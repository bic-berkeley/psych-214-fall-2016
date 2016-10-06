#- Calculate mean across columns
#- Expand to (173, N) shape using np.outer
#- Subtract from data array to remove mean over columns (row means)
#- Put result into array X
row_means = np.outer(np.mean(arr, axis=1), np.ones(N))
X = arr - row_means
