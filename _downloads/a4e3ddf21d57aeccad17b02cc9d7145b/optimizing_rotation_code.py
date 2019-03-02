""" Optimizing rotation exercise
"""

#: standard imports
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)  # print arrays to 4 DP
import nibabel as nib

#: gray colormap and nearest neighbor interpolation by default
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'

#: rotations module
from rotations import x_rotmat, y_rotmat, z_rotmat

#: the first volume of ds107_sub012_t1r2.nii
img_4d = nib.load('ds107_sub012_t1r2.nii')
data = img_4d.get_data()
vol0 = data[..., 0]

#: the secretly rotated image
rotated_img = nib.load('secret_rotated_volume.nii')
rotated_vol0 = rotated_img.get_data()
rotated_vol0.shape

#: slices on z, y, and x axis from 
fig, axes = plt.subplots(3, 2, figsize=(10, 15))
axes[0, 0].imshow(vol0[:, :, 17])
axes[0, 1].imshow(rotated_vol0[:, :, 17])
axes[1, 0].imshow(vol0[:, 31, :])
axes[1, 1].imshow(rotated_vol0[:, 31, :])
axes[2, 0].imshow(vol0[31, :, :])
axes[2, 1].imshow(rotated_vol0[31, :, :])

#- Get correlation mismatch metric from `optimizing_space`, paste here

#: affine_transform function
from scipy.ndimage import affine_transform

#- Make apply_rotations function, accepting `vol_arr` and `rotations`
#- vector, returning image with rotations applied.

#: You could try this quick check that 0 rotations give the same
# output back
not_changed = apply_rotations(rotated_vol0, [0, 0, 0])
assert np.allclose(not_changed, rotated_vol0)

#- Make a cost function, that
#- * is called 'cost_function'
#- * accepts a vector of rotations as input
#- * applies the vector of rotations to `rotated_vol0` from the global
#-   scope
#- * returns the mismatch metric for the transformed copy of
#-   `rotated_vol0` and `vol0`

#: a quick check the cost function returns the current value without rotations
current = correl_mismatch(vol0, rotated_vol0)
redone = cost_function([0, 0, 0])
assert np.allclose(current, redone)

#: get fmin_powell
from scipy.optimize import fmin_powell

#- Call optimizing function and collect best estimates for rotations


#- Use 'apply_rotations' and the estimated parameters to un-rotate the
#- rotated image
#- Put the new un-rotated image into a variable `best_vol0`

#- slices on z, y, and x axis from original and un-rotated image
