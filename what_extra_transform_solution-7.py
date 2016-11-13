#- Work out what transform has been added in the new affine
extra = moved_img.affine.dot(npl.inv(orig_img.affine))
extra
# array([[  0.9553,  -0.2955,   0.    , -10.    ],
# [  0.2955,   0.9553,   0.    , -12.    ],
# [  0.    ,  -0.    ,   1.    , -15.    ],
# [  0.    ,   0.    ,   0.    ,   1.    ]])
