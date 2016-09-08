""" Remove doctest snippets from ReST code, replace title, link to solutions

Process ReST doc with solutions to remove doctest code, replace title, and add
sphinx ``:doc:`` link to solutions document.

Doctests starting with ">>> #:" we leave in the source.

Doctest lines starting ">>> #-" we leave in place.

Doctests lines starting ">>> " and followed by any other doctest stuff, we
remove up until the first empty line.
"""

import sys
from os.path import basename, splitext
import re
import argparse

SECTION_CHARS=r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

HEADER_FMT = """{underline}
{title}
{underline}

For code template see: :download:`{template_name}`;
For solutions see: :doc:`{solution_name}`.
"""

def is_section_line(line):
    if line == '':
        return False
    char0 = line[0]
    if char0 not in SECTION_CHARS:
        return False
    return all(c == char0 for c in line.strip())


def process_rst(contents):
    exercise_page = []
    doctest_blocks = []  # List contains all doctest blocks
    doctest_block = []  #  A block to contain current doctest
    state = 'rest'
    underline_char = None
    title = None
    for line in contents.splitlines(True):
        sline = line.strip()
        if state in ('doctest', 'doctest-keeper'):
            if sline == '':
                exercise_page += doctest_block + ['\n']
                doctest_blocks.append(doctest_block)
                doctest_block = []
                state = 'rest'
            elif state == 'doctest-keeper' or sline.startswith('>>> #-'):
                doctest_block.append(line)
            else:
                continue
        elif state == 'rest':
            if sline.startswith('>>> #:'):  # Keep this whole doctest block
                state = 'doctest-keeper'
                doctest_block.append(line)
            elif sline.startswith('>>> #-'):  # Keep just this line
                doctest_block.append(line)
            elif sline.startswith('>>> '):  # Simply remove
                state = 'doctest'
            elif underline_char is None and is_section_line(line):
                state = 'title'
                underline_char = line[0]
            else:
                exercise_page.append(line)
        elif state == 'title':  # Knock off header
            state = 'post-title'
            title = sline
        elif state == 'post-title':
            assert is_section_line(line)
            state = 'rest'
    if doctest_block:
        doctest_blocks.append(doctest_block)
        exercise_page += doctest_block
    code_template = process_doctest_blocks(doctest_blocks)
    return ''.join(exercise_page), code_template, title, underline_char


def process_doctest_blocks(doctest_blocks):
    return '\n\n'.join(process_doctest_block(dtb) for dtb in doctest_blocks)


DOCTEST_RE = re.compile('^(\s*)(>>>|...) ')


def process_doctest_block(doctest_block):
    return ''.join([DOCTEST_RE.sub('', line) for line in doctest_block])


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("solution_fname")
    parser.add_argument("--new-title")
    parser.add_argument("--out-page")
    parser.add_argument("--out-code")
    return parser


def write_or_print(out, content):
    if out == '0':
        return
    if out == '-':
        sys.stdout.write(content)
        return
    with open(out, 'wt') as fobj:
        fobj.write(content)


SOLUTION_RE = re.compile("(solutions?)")


def main():
    args = get_parser().parse_args()
    in_fname = args.solution_fname
    with open(in_fname, 'rt') as fobj:
        contents = fobj.read()
    processed, code_template, title, u_char = process_rst(contents)
    if title is None:
        raise RuntimeError("Could not find title for page")
    new_title = (args.new_title if args.new_title
                 else title.replace('solution', 'exercise'))
    out_page = (args.out_page if args.out_page
                else SOLUTION_RE.sub('exercise', in_fname))
    out_code = (args.out_code if args.out_code
                else splitext(SOLUTION_RE.sub('code', in_fname))[0] + '.py')
    code_template = '""" {}\n"""\n'.format(new_title) + code_template
    header = HEADER_FMT.format(underline=u_char * len(new_title),
                               title=new_title,
                               solution_name=splitext(basename(in_fname))[0],
                               template_name=basename(out_code))
    write_or_print(out_page, header + processed)
    write_or_print(out_code, code_template)


if __name__ == '__main__':
    main()
