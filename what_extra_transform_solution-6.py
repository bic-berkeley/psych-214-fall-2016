#: Get the new image affine
moved_img = nib.load('ds114_sub009_highres_moved.img')
moved_img.affine
# array([[   0.9416,   -0.4311,   -0.0586,  -98.8336],
# [   0.336 ,    1.1887,    0.2264, -164.1377],
# [  -0.0215,   -0.3028,    0.9723, -158.4178],
# [   0.    ,    0.    ,    0.    ,    1.    ]])