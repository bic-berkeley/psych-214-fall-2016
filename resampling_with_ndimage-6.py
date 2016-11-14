from rotations import x_rotmat  # from rotations.py
# rotation matrix for rotation of 0.2 radians around x axis
M = x_rotmat(0.2)
M
# array([[ 1.    ,  0.    ,  0.    ],
# [ 0.    ,  0.9801, -0.1987],
# [ 0.    ,  0.1987,  0.9801]])
translation = [1, 2, 3]  # Translation from I to J
translation
# [1, 2, 3]
