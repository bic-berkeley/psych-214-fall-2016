def glm(X, Y):
    """ Compute GLM on design `X` and data `Y`
# ...
    Parameters
    ----------
    X : ndarray ahdpe (n, p)
        design matrix, n observations by p columns.
    Y : ndarray shape (n,) or (n,1)
        data.
# ...
    Returns
    -------
    beta : ndarray shape (p,)
       estimated parameters for model `X`
    residual_ss : float
       sum of squares of residuals
    df_error : float
        Degrees of freedom due to error.
    """
    B = npl.pinv(X).dot(Y)
    resid = Y - X.dot(B)
    df = X.shape[0] - npl.matrix_rank(X)
    return B, resid.T.dot(resid), df
