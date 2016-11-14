E = third_affine.dot(second_affine)
E_inv = npl.inv(E)
E_inv.dot(combined)
# array([[ 1.    ,  0.    , -0.    ,  0.    ],
# [ 0.    ,  0.9801,  0.1987,  0.    ],
# [ 0.    , -0.1987,  0.9801,  0.    ],
# [ 0.    ,  0.    ,  0.    ,  1.    ]])
