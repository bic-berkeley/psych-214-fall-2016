B = npl.pinv(X).dot(Y)
fitted = X.dot(B)
E = Y - fitted
sigma_2 = np.sum(E ** 2, axis=0) / df_error
# c and c_b_cov are the same as before, but recalculate anyway
c = np.array([0, 1])
c_b_cov = c.dot(npl.pinv(X.T.dot(X))).dot(c)
t = c.T.dot(B) / np.sqrt(sigma_2 * c_b_cov)
t.shape
# (21604,)
