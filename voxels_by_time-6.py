voxels_by_time = data.reshape((n_voxels, n_trs))
std_devs_vectorized = np.std(voxels_by_time, axis=0)
assert np.allclose(std_devs_vectorized, std_devs)
