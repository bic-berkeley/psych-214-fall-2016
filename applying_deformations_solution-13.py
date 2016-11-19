#- * get mapping from voxels in TPM to voxels in the subject image;
#- * resample the subject image into the grid of the TPM image using
#-   this mapping.
from scipy.ndimage import map_coordinates
vox2vox_mapping = nib.affines.apply_affine(npl.inv(subject_img.affine), deformations_data)
for_map_coords = vox2vox_mapping.transpose(3, 0, 1, 2)
subject_into_tpm = map_coordinates(subject_data, for_map_coords)
subject_into_tpm.shape
# (121, 145, 121)
