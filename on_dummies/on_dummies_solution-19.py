def glm(X,Y):
    """
    input:
      X: design matrix, n observations times p columns
      Y: data (n,1)
    returns beta, residual_var, df_residual_var
    """
    B = npl.pinv(X).dot(Y)
    resid = Y - X.dot(B)
    df = X.shape[0] - npl.matrix_rank(X)
    return B, resid.T.dot(resid), df
# >>>

X0 = X.dot([1, 1]).reshape(n,1)
b, rss, df = glm(X,Y)
tstat = c.T.dot(b)/np.sqrt((rss/df)*c.T.dot(iXtX).dot(c))
b0, rss0, df0 = glm(X0,Y)
nu1 = m - npl.matrix_rank(X0)
Fstat = ((rss0 - rss)/nu1)/(rss/df_error)
print(tstat, np.sqrt(Fstat))
