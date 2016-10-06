#- Calculate the SD across voxels for each volume
#- Identify the outlier volume
voxels_by_time = data.reshape((-1, data.shape[-1]))
stds = np.std(voxels_by_time, axis=0)
np.argmax(stds)
# 0
