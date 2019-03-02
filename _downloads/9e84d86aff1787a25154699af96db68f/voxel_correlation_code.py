""" Voxel correlation exercise
"""
#: compatibility with Python 2
from __future__ import print_function, division

#: import common modules
import numpy as np  # the Python array package
import matplotlib.pyplot as plt  # the Python plotting package
import nibabel as nib

#- import events2neural from stimuli module

#- Load the ds114_sub009_t2r1.nii image

#- Get the number of volumes in ds114_sub009_t2r1.nii

#: TR
TR = 2.5

#- Call the events2neural function to generate the on-off values for
#- each volume.  Plot these values.

#- Drop the first 4 volumes, and the first 4 on-off values.

#- Make a brain-volume-size array of 0 to hold the correlations

#- Loop over all voxel indices.
#- Extract the voxel time courses at each voxel.
#- Get correlation value for voxel time course with on-off vector.
#- Fill value in the correlations array.

#- Plot the middle slice of the third axis from the correlations array
