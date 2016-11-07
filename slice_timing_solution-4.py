#: Load the image 'ds114_sub009_t2r1.nii' with nibabel
# Get the data array from the image
import nibabel as nib
img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
data.shape
# (64, 64, 30, 173)
