#- Try a few plots of binarized slices and other stuff to find a good
#- threshold
pct_99 = np.percentile(subvolume, 99)
binarized_subvolume = subvolume > pct_99
plt.imshow(binarized_subvolume[:, :, 20], cmap='gray')
# <...>
