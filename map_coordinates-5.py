# Resample using affine_transform
from scipy.ndimage import affine_transform
mat, vec = nib.affines.to_matvec(struct_vox2mean_vox)
resampled_mean = affine_transform(mean_bold_data, mat, vec,
                                  output_shape=structural_data.shape)
