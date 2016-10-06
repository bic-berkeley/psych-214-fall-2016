#- Reshape 4D array to 2D array n_voxels by n_volumes
data_2d = np.reshape(data, (n_voxels, data.shape[-1]))
