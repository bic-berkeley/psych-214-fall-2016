t_3d = t.reshape(data.shape[:3])
t_3d.shape
# (64, 64, 30)
plt.imshow(t_3d[:, :, 15], cmap='gray')
# <...>
