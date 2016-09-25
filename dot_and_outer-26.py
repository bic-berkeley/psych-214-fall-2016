de_meaned = arr.copy()
for i in range(arr.shape[0]):  # iterate over rows
    de_meaned[i] = de_meaned[i] - row_means[i]
# The rows now have very near 0 mean
de_meaned.mean(axis=1)
# array([  1.48029737e-16,   0.00000000e+00,   2.96059473e-16,
# 2.96059473e-16])
