""" Slice timing exercise
"""
#: Compatibility with Python 2
from __future__ import print_function  # print('me') instead of print 'me'
from __future__ import division  # 1/2 == 0.5, not 0

#: Import common modules
import numpy as np  # the Python array package
np.set_printoptions(precision=4, suppress=True)  # print to 4 DP
import matplotlib.pyplot as plt  # the Python plotting package
import nibabel as nib

#: Set defaults for plotting
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'

#: Load the image 'ds114_sub009_t2r1.nii' with nibabel
# Get the data array from the image
import nibabel as nib
img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
data.shape

#: Remove the first volume by slicing
fixed_data = data[..., 1:]
fixed_data.shape

#- Slice out time series for voxel (23, 19, 0)
#- Slice out time series for voxel (23, 19, 1)
#- Plot both these time series against volume number, on the same graph

#: The time between scans
TR = 2.5

#- Make time vector containing start times in second of each volume,
#- relative to start of first volume.
#- Call this `slice_0_times`

#- Make time vector containing start times in seconds of z slice 1,
#- relative to start of first volume.
#- Call this `slice_1_times`

#- Plot first 10 values of slice 0 times against first 10 of slice 0
#- time series;
#- Plot first 10 values of slice 1 times against first 10 of slice 1
#- time series.
#- Use ':+' marker

#- Import `InterpolatedUnivariateSpline` from `scipy.interpolate`
#- Make a new linear (`k=1`) interpolation object for slice 1, with
#- slice 1 times and values.

#- Call interpolator with `slice_0_times` to get estimated values

#- Plot first 10 values of slice 0 times against first 10 of slice 0
#- time series;
#- Plot first 10 values of slice 1 times against first 10 of slice 1
#- time series;
#- Plot first 10 values of slice 0 times against first 10 of
#- interpolated slice 1 time series.

#- Copy old data to a new array

#- loop over all x coordinate values
#- loop over all y coordinate values
#- extract the time series at this x, y coordinate for slice 1;
#- make a linear interpolator object with the slice 1 times and the
#- extracted time series;
#- resample this interpolator at the slice 0 times;
#- put this new resampled time series into the new data at the same
#- position.

#- Make acquisition_order vector, length 30, with values:
#- 0, 15, 1, 16 ... 14, 29

#- Divide acquisition_order by number of slices, multiply by TR

#- For each z coordinate (slice index):
#- # Make `slice_z_times` vector for this slice
#- ## For each x coordinate:
#- ### For each y coordinate:
#- #### extract the time series at this x, y, z coordinate;
#- #### make a linear interpolator object with the `slice_z_times` and
#-      the extracted time series;
#- #### resample this interpolator at the slice 0 times;
#- #### put this new resampled time series into the new data at the
#-      same position
