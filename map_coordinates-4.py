mean_mm2vox = npl.inv(bold_img.affine)
struct_vox2mean_vox = mean_mm2vox.dot(structural_img.affine)
struct_vox2mean_vox
# array([[ -0.2497,   0.0151,  -0.0027,  63.5174],
# [  0.0115,   0.3242,   0.0137,   1.1053],
# [ -0.0034,  -0.0176,   0.2496, -27.7359],
# [  0.    ,   0.    ,   0.    ,   1.    ]])
