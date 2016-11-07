#- Plot first 10 values of slice 0 times against first 10 of slice 0
#- time series;
#- Plot first 10 values of slice 1 times against first 10 of slice 1
#- time series;
#- Plot first 10 values of slice 0 times against first 10 of
#- interpolated slice 1 time series.
plt.plot(slice_0_times[:10], slice_0_ts[:10], ':+')
# [...]
plt.plot(slice_1_times[:10], slice_1_ts[:10], ':+')
# [...]
plt.plot(slice_0_times[:10], slice_1_ts_est[:10], 'kx')
# [...]
