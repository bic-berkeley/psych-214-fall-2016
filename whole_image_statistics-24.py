import scipy.stats as stats
t_dist = stats.t(df_error)
p = 1 - t_dist.cdf(t)
p.shape
# (21604,)
p_3d = np.zeros(data.shape[:3])
p_3d[mask] = p
plt.imshow(p_3d[:, :, 15], cmap='gray')
# <...>
