""" Remove doctest snippets from ReST code, replace title, link to solutions

Process ReST doc with solutions to remove doctest code, replace title, and add
sphinx ``:doc:`` link to solutions document.

The code operates on a "template" page.  From the template page, the code can
(and will by default) generate a

* code template file, with a code skeleton to fill out the exercise;
* ReST exercise file, to read, alongside the code template, with more
  detailed instructions;
* ReST solution file, with solutions to the exercises - gemerally a superset of
  the exercise page;

******************
Doctest processing
******************

A doctest starts with a `>>> ` prompt, and ends at the first blank line.

* Doctests starting with ">>> #:" we leave in the source unmodified;
* Doctest lines starting ">>> #-" we leave in place, but we remove the other
  lines in the doctest;
* Doctests lines starting ">>> " and followed by any other doctest stuff, we
  remove up until the first empty line.

************
Other markup
************

A line ``.. solution-start`` starts off a block of markup that defines which
text goes into the solution, the exercise and the code skeleton.

From ``.. solution-start`` up to any other ``.. solution-`` line, goes into the
solution unmodified, but not into the exercise or code skeleton.

If there is a ``.. solution-replace`` line, from that line, until ``..
solution-replace-code`` or ``.. solution-end``, goes into the exercise, but not
the code template.

If there is a ``.. solution-replace-code`` line, from that line, until ``..
solution-replace`` or ``.. solution-end``, goes into the code template, but not
the exercise.
"""

import sys
from os.path import basename, splitext
import re
from textwrap import dedent
import argparse

SECTION_CHARS=r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

HEADER_FMT = """{underline}
{title}
{underline}

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
                extra_code = []
                solution_page.pop()
            else:
                exercise_page.append(line)
        elif state == 'in-solution':
            if sline == '.. solution-replace':
                state = 'replace-in-exercise'
                solution_page.pop()
            elif sline == '.. solution-replace-code':
                state = 'replace-in-code'
                doctest_block = []
                solution_page.pop()
            elif sline == '.. solution-end':
                state = 'rest'
                solution_page.pop()
        elif state == 'replace-in-exercise':
            solution_page.pop()
            if sline == '.. solution-end':
                if extra_code:
                    doctest_blocks.append(
                        dedent(''.join(extra_code)))
                state = 'rest'
            elif sline == '.. solution-replace-code':
                state = 'replace-in-code'
                doctest_block = []
            else:
                exercise_page.append(line)
        elif state == 'replace-in-code':
            solution_page.pop()
            if sline == '.. solution-end':
                if extra_code:
                    doctest_blocks.append(
                        dedent(''.join(extra_code)))
                state = 'rest'
            elif sline == '.. solution-replace':
                state = 'replace-in-exercise'
            else:
                extra_code.append(line)
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


DOCTEST_RE = re.compile('^(\s*)(>>>|\.\.\.) ?')


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
                               title=new_title)
    header_extras = []
    if exercise_code not in ('', 'none'):  # Empty string disables
        header_extras.append(
            '* For code template see: :download:`{}`'.format(
                basename(exercise_code)))
        write_or_print(exercise_code, code_template)
    if solution_page not in ('', 'none'):  # Empty string disables
        header_extras.append(
            '* For solution see: :doc:`{}`'.format(
                basename(splitext(solution_page)[0])))
        write_or_print(solution_page, soln_rst)
    if exercise_page not in ('', 'none'):  # Empty string disables
        extras = ';\n'.join(header_extras) + '.\n\n'
        write_or_print(exercise_page, header + extras + ex_rst)


if __name__ == '__main__':
    main()
