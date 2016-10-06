#- Loop over all voxel indices.
#- Extract the voxel time courses at each voxel.
#- Get correlation value for voxel time course with on-off vector.
#- Fill value in the correlations array.
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        for k in range(data.shape[2]):
            vox_values = data[i, j, k]
            correlations[i, j, k] = np.corrcoef(time_course, vox_values)[1, 0]
