#- Make the mean volume (mean over the last axis)
#- Show the middle slice (slicing over the third axis)
mean_vol = data.mean(axis=-1)
plt.imshow(mean_vol[:, :, 14], cmap='gray')
# <...>
