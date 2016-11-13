#- Use affine_transform to resample from `rotated_vol0` using the transform.
#- Get the result into a variable `derotated_vol0`
from scipy.ndimage import affine_transform
derotated_vol0 = affine_transform(rotated_vol0, M)
derotated_vol0.shape
# (64, 64, 35)
