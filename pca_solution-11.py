#- Row means copied N times to become a 2 by N array
row_means = np.outer(row_means, np.ones(N))
row_means.shape
# (2, 122880)
