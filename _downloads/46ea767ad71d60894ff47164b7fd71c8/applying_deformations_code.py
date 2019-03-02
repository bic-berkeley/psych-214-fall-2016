""" Applying deformations exercise
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

#: load y_ds107_sub012_highres.nii with nibabel
# get the image array data
deformations_img = nib.load('y_ds107_sub012_highres.nii')
deformations_data = deformations_img.get_data()
deformations_data.shape

#: remove length-1 4th dimension from deformation data
deformations_data = np.squeeze(deformations_data)
deformations_data.shape

#: get original TPM.nii 3D shape and affine
tpm_shape = deformations_data.shape[:3]
tpm_affine = deformations_img.affine
tpm_affine

#: load the template image we will resample from
template_img = nib.load('mni_icbm152_t1_tal_nlin_asym_09a.nii')
template_data = template_img.get_data()
template_data.shape

#: voxels in TPM.nii to voxels in mni_icbm152_t1_tal_nlin_asym_09a.nii
# Matrix multiplication is right to left
vox2vox = npl.inv(template_img.affine).dot(tpm_affine)
vox2vox

#: to mat and vec
mat, vec = nib.affines.to_matvec(vox2vox)
mat
vec

#: resample MNI template onto TPM grid
from scipy.ndimage import affine_transform
template_into_tpm = affine_transform(template_data, mat, vec,
                                     output_shape=tpm_shape)
template_into_tpm.shape

#: plot the template image resampled onto the TPM grid
plt.imshow(template_into_tpm[:, :, 60])

#: load the subject data that we will resample from
subject_img = nib.load('ds107_sub012_highres.nii')
subject_data = subject_img.get_data()
subject_data.shape

#- * get mapping from voxels in TPM to voxels in the subject image;
#- * resample the subject image into the grid of the TPM image using
#-   this mapping.

#- show an example slice from the resampled template and resampled
#- subject
