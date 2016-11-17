third_with_second = combined.dot(npl.inv(first_affine))
third_with_second  # doctest: +SKIP
# array([[  0.9211,  -0.    ,   0.3894,  10.    ],
# [  0.    ,   1.    ,   0.    ,  20.    ],
# [ -0.3894,  -0.    ,   0.9211,  30.    ],
# [  0.    ,   0.    ,   0.    ,   1.    ]])
