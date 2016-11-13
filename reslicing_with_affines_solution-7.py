#- Get `mean_vox2mm` mapping
#- Get `mm2struct_vox` mapping
#- Calculate `mean_vox2struct_vox`
mean_vox2mm = bold_img.affine
mm2struct_vox = npl.inv(structural_img.affine)
mean_vox2struct_vox = mm2struct_vox.dot(mean_vox2mm)
mean_vox2struct_vox
# array([[  -3.9954,    0.1836,   -0.0536,  252.0885],
# [   0.1432,    3.0686,   -0.1663,  -17.1005],
# [  -0.0436,    0.2185,    3.9938,  113.2972],
# [   0.    ,    0.    ,    0.    ,    1.    ]])
