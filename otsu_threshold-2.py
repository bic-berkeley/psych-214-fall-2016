cameraman_1d = cameraman.ravel()
n_bins = 128
plt.hist(cameraman_1d, bins=n_bins)
# (...)
counts, edges = np.histogram(cameraman, bins=n_bins)
bin_centers = edges[:-1] + np.diff(edges) / 2.
