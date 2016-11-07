#- Slice out time series for voxel (23, 19, 0)
#- Slice out time series for voxel (23, 19, 1)
#- Plot both these time series against volume number, on the same graph
slice_0_ts = fixed_data[23, 19, 0, :]
slice_1_ts = fixed_data[23, 19, 1, :]
plt.plot(slice_0_ts)
# [...]
plt.plot(slice_1_ts)
# [...]
