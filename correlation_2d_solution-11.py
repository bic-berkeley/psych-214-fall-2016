#- Loop over voxels filling in correlation at this voxel
for i in range(n_voxels):
    correlations_1d[i] = np.corrcoef(time_course, data_2d[i, :])[0, 1]
