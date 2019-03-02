""" Correlation per voxel, in 2D
"""

#: Standard imports
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

#- import events2neural from stimuli module

#- Load the ds114_sub009_t2r1.nii image

#- Get the number of volumes in ds114_sub009_t2r1.nii

#: TR
TR = 2.5

#- Call events2neural to give on-off values for each volume

#- Drop the first 4 volumes, and the first 4 on-off values

#- Calculate the number of voxels (number of elements in one volume)

#- Reshape 4D array to 2D array n_voxels by n_volumes

#- Make a 1D array of size (n_voxels,) to hold the correlation values

#- Loop over voxels filling in correlation at this voxel

#- Or (much faster) use pearson_2d function

#- Reshape the correlations array back to 3D

#- Check you get the same answer when selecting a voxel time course
#- and running the correlation on that time course.  One example voxel
#- could be the voxel at array coordinate [42, 32, 19]

#- Plot the middle slice of the third axis from the correlations array
