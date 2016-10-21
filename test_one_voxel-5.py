y = voxel_time_course
y_hat = X.dot(beta_hat)
residuals = y - y_hat
# Residual sum of squares
RSS = np.sum(residuals ** 2)
# Degrees of freedom: n - no independent columns in X
df = X.shape[0] - npl.matrix_rank(X)
# Mean residual sum of squares
MRSS = RSS / df
# This is our s^2
s2_hat = MRSS
print(s2_hat)
# 247.9375...
print(np.sqrt(s2_hat))
# 15.7460...
