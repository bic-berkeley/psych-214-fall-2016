#: import events2neural from stimuli module
from stimuli import events2neural

#: Load the ds114_sub009_t2r1.nii image
img = nib.load('ds114_sub009_t2r1.nii')

#: Get the number of volumes in ds114_sub009_t2r1.nii
n_trs = img.shape[-1]
