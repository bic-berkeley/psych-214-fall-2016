df_error = n - npl.matrix_rank(X)
df_error
# 167
n
# 169
fitted = X.dot(B)
E = Y - fitted
E.shape
# (169, 122880)
sigma_2 = np.sum(E ** 2, axis=0) / df_error
c_b_cov = c.dot(npl.pinv(X.T.dot(X))).dot(c)
c_b_cov
# 0.0238...
