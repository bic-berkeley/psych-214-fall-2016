#- loop over all x coordinate values
#- loop over all y coordinate values
#- extract the time series at this x, y coordinate for slice 1;
#- make a linear interpolator object with the slice 1 times and the
#- extracted time series;
#- resample this interpolator at the slice 0 times;
#- put this new resampled time series into the new data at the same
#- position.
for x in range(fixed_data.shape[0]):
    for y in range(fixed_data.shape[1]):
        time_series = fixed_data[x, y, 1, :]
        interp = InterpolatedUnivariateSpline(slice_1_times, time_series, k=1)
        new_series = interp(slice_0_times)
        new_data[x, y, 1, :] = new_series
