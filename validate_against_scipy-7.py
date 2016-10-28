X2 = np.zeros((n, 2))
X2[:10, 0] = 1
X2[10:, 1] = 1
X2
# array([[ 1.,  0.],
# [ 1.,  0.],
# [ 1.,  0.],
# [ 1.,  0.],
# [ 1.,  0.],
# [ 1.,  0.],
# [ 1.,  0.],
# [ 1.,  0.],
# [ 1.,  0.],
# [ 1.,  0.],
# [ 0.,  1.],
# [ 0.,  1.],
# [ 0.,  1.],
# [ 0.,  1.],
# [ 0.,  1.],
# [ 0.,  1.],
# [ 0.,  1.],
# [ 0.,  1.],
# [ 0.,  1.],
# [ 0.,  1.]])
B2 = npl.pinv(X2).dot(y)
E2 = y - X2.dot(B2)
c2 = np.array([-1, 1])
df = n - npl.matrix_rank(X2)
sigma_2 = np.sum(E2 ** 2) / df
c_b_cov = c2.dot(npl.pinv(X2.T.dot(X2))).dot(c2)
t = c2.dot(B2) / np.sqrt(sigma_2 * c_b_cov)
t
# -0.30792...
t_dist = scipy.stats.t(df=df)
# One-tailed p value, for negative value
p_value_2 = t_dist.cdf(t)
p_value_2
# 0.38083...
# Two-tailed p value
p_value_2 * 2
# 0.76167...
