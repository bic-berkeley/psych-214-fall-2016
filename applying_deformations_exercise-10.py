#: resample MNI template onto TPM grid
from scipy.ndimage import affine_transform
template_into_tpm = affine_transform(template_data, mat, vec,
                                     output_shape=tpm_shape)
template_into_tpm.shape
# (121, 145, 121)
