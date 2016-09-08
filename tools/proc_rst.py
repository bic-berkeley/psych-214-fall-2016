""" Remove doctest snippets from ReST code, replace title, link to solutions

Process ReST doc with solutions to remove doctest code, replace title, and add
sphinx ``:doc:`` link to solutions document.

Doctests starting with ">>> #:" we leave in the source.

Doctests starting with ">>> #-" we remove completely.

Doctests starting ">>> " and followed by anything else, we replace with the
doctest marker "::  >>> # Your code here"
"""

from os.path import split as psplit, splitext
import argparse

SECTION_CHARS=r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

HEADER_FMT = """{underline}
{title}
{underline}

For solutions see :doc:`{solution_name}`
"""

DOCTEST_MARKER = '::\n\n    >>> # Your code here\n\n'

def is_section_line(line):
    if line == '':
        return False
    char0 = line[0]
    if char0 not in SECTION_CHARS:
        return False
    return all(c == char0 for c in line.strip())


def process_rst(contents):
    exercise_contents = []
    state = 'rest'
    underline_char = None
    for line in contents.splitlines(True):
        sline = line.strip()
        if state in ('doctest', 'doctest-loser', 'doctest-keeper'):
            if state == 'doctest-keeper':
                exercise_contents.append(line)
            if sline == '':
                state = 'rest'
            continue
        elif state == 'rest':
            if sline.startswith('>>> #:'):  # Keep this doctest
                state = 'doctest-keeper'
            elif sline.startswith('>>> #-'):  # Drop this one completely
                state = 'doctest-loser'
                continue
            elif sline.startswith('>>> '):  # Replace this with Your code here
                state = 'doctest'
                line = DOCTEST_MARKER
            elif underline_char is None and is_section_line(line):
                state = 'title'
                underline_char = line[0]
                continue
            exercise_contents.append(line)
        elif state == 'title':  # Knock of header
            state = 'post-title'
        elif state == 'post-title':
            assert is_section_line(line)
            state = 'rest'
    out = ''.join(exercise_contents)
    return out, underline_char


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("in_fname")
    parser.add_argument("new_title")
    return parser


def main():
    args = get_parser().parse_args()
    with open(args.in_fname, 'rt') as fobj:
        contents = fobj.read()
    processed, u_char = process_rst(contents)
    if u_char is None:
        raise RuntimeError("Could not find title for page")
    solution_doc = splitext(psplit(args.in_fname)[1])[0]
    header = HEADER_FMT.format(underline=u_char * len(args.new_title),
                               title=args.new_title,
                               solution_name=solution_doc)
    print(header + processed)


if __name__ == '__main__':
    main()
