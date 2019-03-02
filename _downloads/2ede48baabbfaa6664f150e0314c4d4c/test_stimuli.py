""" Test stimuli module

Run tests with::

    py.test test_stimuli.py
"""

import os

import numpy as np
import numpy.testing as npt

import stimuli

# Example onset, duration, amplitude triplets
COND_TEST = """\
10    6.0    1
20    4.0    2
24    2.0    0.1"""

# Name of file to write for testing
COND_TEST_FNAME = 'cond_test1.txt'


def test_events2neural():
    # test events2neural function
    # Write condition test file
    with open(COND_TEST_FNAME, 'wt') as fobj:
        fobj.write(COND_TEST)
    # Read it back
    neural = stimuli.events2neural(COND_TEST_FNAME, 2, 16)
    # Expected values for tr=2, n_trs=16
    expected = np.zeros(16)
    expected[5:8] = 1
    expected[10:12] = 2
    expected[12] = 0.1
    npt.assert_array_equal(neural, expected)
    neural = stimuli.events2neural(COND_TEST_FNAME, 1, 30)
    # Expected values for tr=1, n_trs=30
    expected = np.zeros(30)
    expected[10:16] = 1
    expected[20:24] = 2
    expected[24:26] = 0.1
    npt.assert_array_equal(neural, expected)
    # Remove test file
    os.unlink(COND_TEST_FNAME)
