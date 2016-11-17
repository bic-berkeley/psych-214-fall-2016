#- Break up `template_vox2subject_vox` into 3x3 `mat` and
#- length 3 `vec`
mat, vec = nib.affines.to_matvec(template_vox2subject_vox)
mat
# array([[-1.    ,  0.    ,  0.    ],
# [-0.    ,  0.7691,  0.    ],
# [-0.    , -0.    ,  1.    ]])
vec
# array([ 90.3506, -18.22  ,  50.6663])
