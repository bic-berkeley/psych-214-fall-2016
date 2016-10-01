""" Correlation per voxel, in 2D
"""

#: Standard imports
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

#: import events2neural from stimuli module
from stimuli import events2neural

#: Load the ds114_sub009_t2r1.nii image
img = nib.load('ds114_sub009_t2r1.nii')

#: Get the number of volumes in ds114_sub009_t2r1.nii
n_trs = img.shape[-1]


#: Call events2neural to give on-off values for each volume
time_course = events2neural('ds114_sub009_t2r1_cond.txt', 2.5, n_trs)

#: Drop the first 4 volumes, and the first 4 on-off values
data = img.get_data()
data = data[..., 4:]
time_course = time_course[4:]

#- Calculate the number of voxels (number of elements in one volume)

#- Reshape 4D array to 2D array n_voxels by n_volumes

#- Make a 1D array of size (n_voxels,) to hold the correlation values

#- Loop over voxels filling in correlation at this voxel

#- Reshape the correlations array back to 3D

#- Plot the middle slice of the third axis from the correlations array
