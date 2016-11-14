def ssd(counts, centers):
    """ Sum of squared deviations from mean """
    n = np.sum(counts)
    mu = np.sum(centers * counts) / n
    return np.sum(counts * ((centers - mu) ** 2))
