#- Use affine_transform to make a copy of the subject image
#- resampled into the array dimensions of the template image
#- Call this resampled copy `subject_resampled`
#- (we are going to use this array later).
#- Use order=1 for the resampling (it is quicker)
from scipy.ndimage import affine_transform
subject_resampled = affine_transform(subject_data, mat, vec,
                                     output_shape=template_data.shape,
                                     order=1)
