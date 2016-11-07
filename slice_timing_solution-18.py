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
for z in range(fixed_data.shape[2]):
    slice_z_times = slice_0_times + time_offsets[z]
    for x in range(fixed_data.shape[0]):
        for y in range(fixed_data.shape[1]):
            time_series = fixed_data[x, y, z, :]
            interp = InterpolatedUnivariateSpline(slice_z_times, time_series, k=1)
            new_series = interp(slice_0_times)
            new_data[x, y, z, :] = new_series
