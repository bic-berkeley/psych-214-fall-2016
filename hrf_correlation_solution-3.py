#- Load the image with nibabel.
#- Get the image data array, print the data shape.
import nibabel as nib
img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
data.shape
# (64, 64, 30, 173)
