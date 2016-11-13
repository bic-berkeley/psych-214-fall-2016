""" Extra transform exercise
"""

#: standard imports
import numpy as np
import numpy.linalg as npl
import matplotlib.pyplot as plt
# print arrays to 4 decimal places
np.set_printoptions(precision=4, suppress=True)
import nibabel as nib

#: gray colormap and nearest neighbor interpolation by default
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'

#: functions to make rotation matrices
from rotations import x_rotmat, y_rotmat, z_rotmat

#: Get the original image affine
import nibabel as nib
orig_img = nib.load('ds114_sub009_highres.nii')
print(orig_img.affine)

#: Get the new image affine
moved_img = nib.load('ds114_sub009_highres_moved.img')
moved_img.affine

#- Work out what transform has been added in the new affine

#- What rotation and translation has been applied?
