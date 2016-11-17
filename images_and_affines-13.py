# This is the same as
F = third_affine.dot(second_affine)
F  # doctest: +SKIP
# array([[  0.9211,   0.    ,   0.3894,  10.    ],
# [  0.    ,   1.    ,   0.    ,  20.    ],
# [ -0.3894,   0.    ,   0.9211,  30.    ],
# [  0.    ,   0.    ,   0.    ,   1.    ]])
np.allclose(third_with_second, F)
# True
