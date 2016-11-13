#- Load structural and BOLD image
#- Print image data shape
#- Print affine from header
bold_img = nib.load('ds114_sub009_t2r1.nii')
print(bold_img.shape)
# (64, 64, 30, 173)
print(bold_img.affine)
# [[  -4.        0.        0.      124.244 ]
# [   0.        3.9345    0.7207 -103.4497]
# [   0.       -0.7207    3.9346  -33.4929]
# [   0.        0.        0.        1.    ]]
structural_img = nib.load('ds114_sub009_highres.nii')
print(structural_img.shape)
# (256, 156, 256)
print(structural_img.affine)
# [[   0.9989   -0.0605    0.0109 -129.8257]
# [   0.0427    1.263     0.2336 -119.0906]
# [  -0.0215   -0.3028    0.9723 -143.4178]
# [   0.        0.        0.        1.    ]]
