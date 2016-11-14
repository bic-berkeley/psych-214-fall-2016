c = c[:, None]
c.shape
# (2, 1)
c_b_cov = c.T.dot(npl.pinv(X.T.dot(X))).dot(c)
c_b_cov
# array([[ 0.0238]])
