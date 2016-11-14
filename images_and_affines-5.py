first_affine = np.eye(4)  # The identity affine
first_affine[:3, :3] = first_rotation
first_affine
# array([[ 1.    ,  0.    ,  0.    ,  0.    ],
# [ 0.    ,  0.9801,  0.1987,  0.    ],
# [ 0.    , -0.1987,  0.9801,  0.    ],
# [ 0.    ,  0.    ,  0.    ,  1.    ]])
