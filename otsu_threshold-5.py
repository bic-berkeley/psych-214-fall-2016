from skimage.filters import threshold_otsu
threshold_otsu(cameraman, n_bins)
# 0.33984375
np.allclose(threshold_otsu(cameraman, n_bins), t)
# True
