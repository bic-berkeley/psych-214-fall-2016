#- loop over all x coordinate values
#- loop over all y coordinate values
#- extract the time series at this x, y coordinate for slice 1;
#- make a linear interpolator object with the slice 1 times and the
#- extracted time series;
#- resample this interpolator at the slice 0 times;
#- put this new resampled time series into the new data at the same
#- position.
