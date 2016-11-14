#- Get affine mapping from template voxels to subject voxels
template_vox2subject_vox = npl.inv(subject_img.affine).dot(template_img.affine)
template_vox2subject_vox
# array([[ -1.    ,   0.    ,   0.    ,  90.3506],
# [ -0.    ,   0.7691,   0.    , -18.22  ],
# [ -0.    ,  -0.    ,   1.    ,  50.6663],
# [  0.    ,   0.    ,   0.    ,   1.    ]])
