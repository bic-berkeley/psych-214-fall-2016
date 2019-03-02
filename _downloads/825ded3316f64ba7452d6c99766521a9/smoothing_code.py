""" Smoothing exercise
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

#: get first volume from functional
import nibabel as nib
img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
vol0 = data[..., 0]

#: get slice over third dimension
mid_slice = vol0[:, :, 14]
plt.imshow(mid_slice)

#: get middle line from middle slice
mid_line = mid_slice[:, 25]
plt.plot(mid_line)

#: Full-width at half-maximum to sigma
def fwhm2sigma(fwhm):
    return fwhm / np.sqrt(8 * np.log(2))

#: Test output of fwhm2sigma for a single FWHM
assert np.allclose(fwhm2sigma(4), 1.698643600576)

#- sigma for FWHM 8?

#: import the Gaussian (normal) distribution function
from scipy.stats import norm
norm_pdf = norm.pdf

#- Work out the +/- limit for the kernel x values;
#- Make a vector `x` to sample the PDF;
#- Get `kernel` vector by sampling the PDF at these x values (mu=0);
#- Work out `kernel_offset`.

#- Convolve image line with kernel
#- Slice out the result we want using kernel_offset
#- Plot smoothed with unsmoothed line

#- Make a new array `smoothed_slice` for smoothed output
#- Loop over first dimension applying kernel as above
#- Loop over second dimension of smoothed image, applying kernel
#- Show with `imshow`

#: import gaussian_filter
from scipy.ndimage import gaussian_filter

#- Use gaussian filter to smooth `mid_slice`

#- Subtract two versions of the smoothed slice, show
