second_affine = np.eye(4)
second_affine[:3, :3] = y_rotmat(0.4)
second_affine
# array([[ 0.9211,  0.    ,  0.3894,  0.    ],
# [ 0.    ,  1.    ,  0.    ,  0.    ],
# [-0.3894,  0.    ,  0.9211,  0.    ],
# [ 0.    ,  0.    ,  0.    ,  1.    ]])
