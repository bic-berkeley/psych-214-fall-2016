#- Calculate c (X.T X) c.T
c_iXtX_ct = c.dot(npl.inv(X.T.dot(X))).dot(c)
c_iXtX_ct
# 0.40000...
