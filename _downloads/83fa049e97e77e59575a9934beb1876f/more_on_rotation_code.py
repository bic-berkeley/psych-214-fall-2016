""" Rotation exercise
"""

#: standard imports
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)  # print arrays to 4 DP
import nibabel as nib

#: gray colormap and nearest neighbor interpolation by default
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'

#: Check import of rotations code
from rotations import x_rotmat, y_rotmat, z_rotmat

#: the first volume of ds107_sub012_t1r2.nii
img_4d = nib.load('ds107_sub012_t1r2.nii')
data = img_4d.get_data()
vol0 = data[..., 0]

#: the resulting rotated image
rotated_img = nib.load('rotated_volume.nii')
rotated_vol0 = rotated_img.get_data()
rotated_vol0.shape

#: slices on z, y, and x axis for original and rotated images
fig, axes = plt.subplots(3, 2, figsize=(10, 15))
axes[0, 0].imshow(vol0[:, :, 17])
axes[0, 1].imshow(rotated_vol0[:, :, 17])
axes[1, 0].imshow(vol0[:, 31, :])
axes[1, 1].imshow(rotated_vol0[:, 31, :])
axes[2, 0].imshow(vol0[31, :, :])
axes[2, 1].imshow(rotated_vol0[31, :, :])

#- Make a 3 by 3 transformation matrix that applies this sequence
#- * 0.1 radians around the x axis, then
#- * 0.2 radians around the y axis, then
#- * 0.3 radians around the z axis.

#- Use affine_transform to resample from `rotated_vol0` using the transform.
#- Get the result into a variable `derotated_vol0`

#- plot slices from the image to see if you got the right transformation.
