""" Test rotations

Run the tests with::

    py.test test_rotations.py
"""

import numpy as np

from rotations import x_rotmat, y_rotmat, z_rotmat

from numpy.testing import assert_almost_equal

EXAMPLE_ROTATIONS = np.linspace(0, np.pi * 5, 100)
RIGHT_ANGLE = np.pi / 2


def test_rotmats():
    # Test rotation functions
    for rot_func in (x_rotmat, y_rotmat, z_rotmat):
        # Check rotation of 0 degrees gives identity matrix
        assert_almost_equal(rot_func(0), np.eye(3))
        # On example rotations, check positive then negative rotation gives
        # identity matrix (0 degree rotation)
        for theta in EXAMPLE_ROTATIONS:
            M = rot_func(theta)
            iM = rot_func(-theta)
            assert_almost_equal(iM.dot(M), np.eye(3))
        # Test rotating twice by 90 degrees gives 180 degree rotation
        M = rot_func(RIGHT_ANGLE)
        assert_almost_equal(M.dot(M), rot_func(np.pi))
        # Test rotating four times by 90 degrees gives 0 degree rotation
        assert_almost_equal(M.dot(M).dot(M).dot(M), np.eye(3))
