""" Tests for proc_rst module

Run with::

    py.test test_proc_rst.py
"""

import sys
from os.path import dirname

sys.path.append(dirname(__file__))

from proc_rst import process_doctest_block


def test_process_doctest_block():
    assert process_doctest_block(['']) == ''
    assert process_doctest_block(['>>> ']) == ''
    assert process_doctest_block(['>>> foo = 1']) == 'foo = 1'
    assert process_doctest_block(['>>> if foo == 1:\n',
                                  '...     bar = 2']) == (
                                      'if foo == 1:\n    bar = 2')
