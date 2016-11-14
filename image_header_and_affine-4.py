import nibabel as nib
img = nib.load('ds107_sub012_highres.nii')
img.affine
# array([[   1.    ,    0.    ,    0.    , -127.    ],
# [   0.    ,    1.    ,    0.    ,  -83.3253],
# [   0.    ,    0.    ,    1.    ,  -90.0533],
# [   0.    ,    0.    ,    0.    ,    1.    ]])
