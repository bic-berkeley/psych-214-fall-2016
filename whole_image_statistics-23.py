t_3d = np.zeros(data.shape[:3])
t_3d[mask] = t
plt.imshow(t_3d[:, :, 15], cmap='gray')
# <...>
