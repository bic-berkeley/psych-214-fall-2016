# Contrast vector selects slope parameter
c = np.array([0, 1])
df = n - npl.matrix_rank(X)
sigma_2 = np.sum(E ** 2) / df
c_b_cov = c.dot(npl.pinv(X.T.dot(X))).dot(c)
t = c.dot(B) / np.sqrt(sigma_2 * c_b_cov)
t
# 0.82220...
