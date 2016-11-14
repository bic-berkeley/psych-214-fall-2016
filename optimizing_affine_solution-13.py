#: the negative correlation mismatch metric
def correl_mismatch(x, y):
    """ Negative correlation between the two images, flattened to 1D
    """
    x_mean0 = x.ravel() - x.mean()
    y_mean0 = y.ravel() - y.mean()
    corr_top = x_mean0.dot(y_mean0)
    corr_bottom = (np.sqrt(x_mean0.dot(x_mean0)) *
                   np.sqrt(y_mean0.dot(y_mean0)))
    return -corr_top / corr_bottom
