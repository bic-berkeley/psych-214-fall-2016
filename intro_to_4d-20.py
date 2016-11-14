# variance across the final (time) axis
var_vol = np.var(data, axis=3)
plt.imshow(var_vol[:, :, 14], cmap='gray')
# <...>
