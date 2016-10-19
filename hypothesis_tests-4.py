# Data vector
y = psychopathy
# Covariate vector
x = clammy
# Contrast vector as column vector
c = np.array([0, 1]).reshape((2, 1))
n = len(y)
# Design matrix
X = np.ones((n, 2))
X[:, 1] = x
# X.T X is invertible
iXtX = npl.inv(X.T.dot(X))
# Least-squares estimate of B
B = iXtX.dot(X.T).dot(y)
e = y - X.dot(B)
# Degrees of freedom of design
rank_x = npl.matrix_rank(X)
# The two columns are not colinear, so rank is 2
rank_x
# 2
# Unbiased estimate of population variance
df_error = n - rank_x
s2_hat = e.dot(e) / df_error
t = c.T.dot(B) / np.sqrt(s2_hat * c.T.dot(iXtX).dot(c))
t
# array([[ 1.914389]])
