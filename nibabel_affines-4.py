# Affine from a 3x3 matrix ('mat') and a translation vector ('vec')
aff = nib.affines.from_matvec(y_rotation, [10, 20, 30])
aff
# array([[  0.9211,   0.    ,   0.3894,  10.    ],
# [  0.    ,   1.    ,   0.    ,  20.    ],
# [ -0.3894,   0.    ,   0.9211,  30.    ],
# [  0.    ,   0.    ,   0.    ,   1.    ]])
