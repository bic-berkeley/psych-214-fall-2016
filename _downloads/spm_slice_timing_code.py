""" SPM slice timing exercise
"""

#: standard imports
import numpy as np
import matplotlib.pyplot as plt
# print arrays to 4 decimal places
np.set_printoptions(precision=4, suppress=True)
import numpy.linalg as npl
import nibabel as nib

#: gray colormap and nearest neighbor interpolation by default
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'

#: save new copy of image with first four volumes dropped
img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
fixed = nib.Nifti1Image(data[..., 4:], img.affine, img.header)
nib.save(fixed, 'fds114_sub009_t2r1.nii')

#: load the fixed "f" image to get parameters
img = nib.load('fds114_sub009_t2r1.nii')
num_slices = img.shape[2]
num_slices

#: get the TR from this image
TR = img.header.get_zooms()[-1]
TR

#: calculate TA
time_for_one_slice = TR / num_slices
TA = TR - time_for_one_slice
TA


#: import the routines for working with the operating system
import os
# Delete file if it exists
if os.path.exists('afds114_sub009_t2r1.nii'):
    os.unlink('afds114_sub009_t2r1.nii')  # delete file

#: import initilization of nipype / MATLAB interface from "introducing
#  nipype" page.
import nipype_settings

#: import slice timing from nipype SPM interfaces
from nipype.interfaces.spm import SliceTiming

#- Initialize the SliceTiming batch object, and fill parameters
#- Run the slice timing on the fixed image `fds114_sub009_t2r1.nii`

#- Run the batch job
