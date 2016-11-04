#- Calculate c (X.T X)^-1 c.T
c_iXtX_ct = c.dot(npl.inv(X.T.dot(X))).dot(c)
c_iXtX_ct
# 0.40000...
