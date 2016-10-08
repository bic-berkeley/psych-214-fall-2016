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

* For code template see: :download:`{template_name}`;
* For solutions see: :doc:`{solution_name}`.
"""

def is_section_line(line):
    if line == '':
        return False
    char0 = line[0]
    if char0 not in SECTION_CHARS:
        return False
    return all(c == char0 for c in line.strip())


def process_rst(contents):
    """ Process solution ReST in `contents` to get title, code and exercise

    See Notes section for detail on doctest processing.

    Parameters
    ----------
    contents : str
        String containing ReSTructured text of solutions.

    Returns
    -------
    exercise_page : str
        ReST text for exercise, with doctest blocks removed, that were not
        labeled for inclusion (see Notes for details).
    code_template : str
        Python code template for students to fill in.  Code template contains
        doctest comments and blocks labeled for inclusion (see Notes).
    title : None or str
        Any title found between overline and underline in the `contents`.  None
        if no such title found.
    underline_char : None or str
        Character used in overline / underline of title.  None if no title
        found.

    Notes
    -----
    A doctest block is continuous list of lines where the first line starts
    with ">>> " and the last line is empty (newline only or newline and space).

    Doctest blocks starting with ">>> #:" we leave unmodified in the
    `exercise_page` and `code_template`.

    Any doctest lines starting ">>> #-" we leave in the `exercise_page` and
    `code_template`, regardless of whether they are in a doctest block.

    Otherwise, remove all doctest blocks.
    """
    exercise_page = []
    doctest_blocks = []  # List contains all doctest blocks
    doctest_block = []  #  A block to contain current doctest
    state = 'rest'
    underline_char = None
    title = None
    solution_page = []
    for line in contents.splitlines(True):
        solution_page.append(line)
        sline = line.strip()
        if state in ('doctest', 'doctest-keeper'):
            if sline == '':
                exercise_page += doctest_block + ['\n']
                doctest_blocks.append(doctest_block)
                doctest_block = []
                state = 'rest'
            elif state == 'doctest-keeper' or sline.startswith('>>> #-'):
                doctest_block.append(line)
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
            elif sline.startswith('.. solution-start'):
                state = 'in-solution'
            else:
                exercise_page.append(line)
        elif state == 'in-solution':
            if sline.startswith('.. solution-replace'):
                state = 'replace-solution'
            elif sline.startswith('.. solution-end'):
                state = 'rest'
        elif state == 'replace-solution':
            if sline.startswith('.. solution-end'):
                state = 'rest'
            else:
                exercise_page.append(line)
                solution_page.pop()
        elif state == 'title':  # Knock off header
            state = 'post-title'
            title = sline
        elif state == 'post-title':
            assert is_section_line(line)
            assert line[0] == underline_char
            state = 'rest'
    if doctest_block:
        doctest_blocks.append(doctest_block)
        exercise_page += doctest_block
    code_template = process_doctest_blocks(doctest_blocks)
    return (''.join(solution_page),
            ''.join(exercise_page),
            code_template, title, underline_char)


def process_doctest_blocks(doctest_blocks):
    return '\n'.join(process_doctest_block(dtb) for dtb in doctest_blocks)


DOCTEST_RE = re.compile('^(\s*)(>>>|...) ?')


def process_doctest_block(doctest_block):
    return ''.join([DOCTEST_RE.sub('', line) for line in doctest_block])


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("solution_fname")
    parser.add_argument("--new-title")
    parser.add_argument("--exercise-page")
    parser.add_argument("--solution-page")
    parser.add_argument("--exercise-code")
    return parser


def write_or_print(out, content):
    if out == '0':
        return
    if out == '-':
        sys.stdout.write(content)
        return
    with open(out, 'wt') as fobj:
        fobj.write(content)


def main():
    args = get_parser().parse_args()
    in_fname = args.solution_fname
    froot, ext = splitext(in_fname)
    with open(in_fname, 'rt') as fobj:
        contents = fobj.read()
    soln_rst, ex_rst, code_template, title, u_char = process_rst(contents)
    if title is None:
        raise RuntimeError("Could not find title for page")
    new_title = (args.new_title if args.new_title
                 else title.replace('solution', 'exercise'))
    solution_page = (froot + '_solution.rst' if args.solution_page is None
                     else args.solution_page)
    exercise_page = (froot + '_exercise.rst' if args.exercise_page is None
                     else args.exercise_page)
    exercise_code = (froot + '_code.py' if args.exercise_code is None
                     else args.exercise_code)
    code_template = '""" {}\n"""\n'.format(new_title) + code_template
    header = HEADER_FMT.format(underline=u_char * len(new_title),
                               title=new_title,
                               solution_name=splitext(basename(in_fname))[0],
                               template_name=basename(exercise_code))
    if solution_page not in ('', 'none'):  # Empty string disables
        write_or_print(solution_page, soln_rst)
    if exercise_page not in ('', 'none'):  # Empty string disables
        write_or_print(exercise_page, header + ex_rst)
    if exercise_code not in ('', 'none'):  # Empty string disables
        write_or_print(exercise_code, code_template)


if __name__ == '__main__':
    main()
