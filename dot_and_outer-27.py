# Use a loop to subtract the mean from each row
de_meaned = arr.copy()
for i in range(arr.shape[0]):  # iterate over rows
    de_meaned[i] = de_meaned[i] - row_means[i]
# The rows now have very near 0 mean
de_meaned.mean(axis=1)
# array([ 0.,  0.,  0.,  0.])
