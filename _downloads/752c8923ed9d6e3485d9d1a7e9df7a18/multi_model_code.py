""" Basic linear modeling
"""
#: Import some standard librares
import numpy as np
# Print to 4 DP
np.set_printoptions(precision=4)
import numpy.linalg as npl
import matplotlib.pyplot as plt
# Set default imshow parameters
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

#: Load the image as an image object
import nibabel as nib
img = nib.load('ds114_sub009_t2r1.nii')

#: Load the image data as an array
# Drop the first 4 3D volumes from the array
# (We already saw that these were abnormal)
data = img.get_data()[..., 4:]

#- Load the pre-written convolved time course
#- Knock off the first four elements

#- Compile the design matrix
#- First column is convolved regressor
#- Second column all ones
#- Hint: investigate "aspect" keyword to ``plt.imshow`` for a nice
#- looking image.

#- Reshape the 4D data to voxel by time 2D
#- Transpose to give time by voxel 2D
#- Calculate the pseudoinverse of the design
#- Apply to time by voxel array to get betas

#- Transpose betas to give voxels by 2 array
#- Reshape into 4D array, with same 3D shape as original data,
#- last dimension length 2

#- Show the middle slice from the first beta volume

#- Show the middle slice from the second beta volume
