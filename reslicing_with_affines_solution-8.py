#- Split `mean_vox2struct_vox` into 3x3 transformation, 3 element
#- translation.
M = mean_vox2struct_vox[:3, :3]
M
# array([[-3.9954,  0.1836, -0.0536],
# [ 0.1432,  3.0686, -0.1663],
# [-0.0436,  0.2185,  3.9938]])
T = mean_vox2struct_vox[:3, 3]
T
# array([ 252.0885,  -17.1005,  113.2972])
