first_affine
# array([[ 1.    ,  0.    ,  0.    ,  0.    ],
# [ 0.    ,  0.9801,  0.1987,  0.    ],
# [ 0.    , -0.1987,  0.9801,  0.    ],
# [ 0.    ,  0.    ,  0.    ,  1.    ]])
np.allclose(E_inv.dot(combined), first_affine)
# True
