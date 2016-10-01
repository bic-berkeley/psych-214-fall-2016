#- Load the image and check the image shape to get the number of TRs
import nibabel as nib
img = nib.load('ds114_sub009_t2r1.nii')
img.shape
# (64, 64, 30, 173)
