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
