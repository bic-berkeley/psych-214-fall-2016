from skimage.filters import threshold_otsu
mean = data.mean(axis=-1)
mean.shape
# (64, 64, 30)
thresh = threshold_otsu(mean)
thresh
# 849.70914...
# The mask has True for voxels above "thresh", False otherwise
mask = mean > thresh
mask.shape
# (64, 64, 30)
plt.imshow(mask[:, :, 15], cmap='gray')
# <...>
data.shape
# (64, 64, 30, 169)
