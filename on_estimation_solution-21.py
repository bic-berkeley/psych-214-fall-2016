# Fit again to original model
y = psychopathy
B = npl.inv(X.T.dot(X)).dot(X.T).dot(y)
B
# array([ 9.8016,  0.8074])

# Fit again to mean-centered model
B_o = npl.inv(X_o.T.dot(X_o)).dot(X_o.T).dot(y)
B_o
# array([ 12.5746,   0.8074])

# The difference in B_o[0] (c) is b * X[:, 1].mean()
B[1] * X[:, 1].mean()
# 2.7729...
B[0] + B[1] * X[:, 1].mean()
# 12.57458...
