t_3d[0, 0, 15]
# nan
np.all(data[0, 0, 15] == 0)
# memmap(True, dtype=bool)
sigma_2_3d = sigma_2.reshape(data.shape[:3])
sigma_2_3d[0, 0, 15]
# 0.0
