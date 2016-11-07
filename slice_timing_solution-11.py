#- Import `InterpolatedUnivariateSpline` from `scipy.interpolate`
#- Make a new linear (`k=1`) interpolation object for slice 1, with
#- slice 1 times and values.
from scipy.interpolate import InterpolatedUnivariateSpline
interp = InterpolatedUnivariateSpline(slice_1_times, slice_1_ts, k=1)
