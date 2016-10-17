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
       sum of squares of residual
    df_error : float
        Degrees of freedom due to error.
    """
    B = npl.pinv(X).dot(Y)
    resid = Y - X.dot(B)
    df = X.shape[0] - npl.matrix_rank(X)
    return B, resid.T.dot(resid), df

X_r = X
X_f = np.column_stack((clammy, X))
b_f, rss_f, df_f = glm(X_f, Y)
b_r, rss_r, df_r = glm(X_r, Y)
nu_1 = npl.matrix_rank(X_f) - npl.matrix_rank(X_r)
f_stat = ((rss_r - rss_f) / nu_1) / (rss_f / df_f)
f_stat
# 6.15949...
