#: Get the original image affine
import nibabel as nib
orig_img = nib.load('ds114_sub009_highres.nii')
print(orig_img.affine)
# [[   0.9989   -0.0605    0.0109 -129.8257]
# [   0.0427    1.263     0.2336 -119.0906]
# [  -0.0215   -0.3028    0.9723 -143.4178]
# [   0.        0.        0.        1.    ]]
