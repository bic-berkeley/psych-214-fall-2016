""" Reslicing with affines exercise
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

#- Load structural and BOLD image
#- Print image data shape
#- Print affine from header

#- Load BOLD image data.  Drop first volume.  Make mean volume
#- Plot an example slice from the mean volume

#- Load structural data, plot example slice

#- Get `mean_vox2mm` mapping
#- Get `mm2struct_vox` mapping
#- Calculate `mean_vox2struct_vox`

#- Split `mean_vox2struct_vox` into 3x3 transformation, 3 element
#- translation.

#: import affine_transform function
from scipy.ndimage import affine_transform

#- Use affine_transform and the tranformation components to resample
#- structural to functional

#- Display example slice from mean vol and resliced structural side by
#- side.

#- Get affine transformation `struct_vox2mean_vox`

#- Reslice mean functional to structural voxel space

#- Display example slices for resliced mean and structural
