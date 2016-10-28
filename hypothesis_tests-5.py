# We already have X, e, rank_x, for the full model, from
# the t calculation
X_f, e_f, rank_f = X, e, rank_x
# Now calculate the same for the reduced model
X_r = np.ones((n, 1))
iXtX_r = npl.inv(X_r.T.dot(X_r))
B_r = iXtX_r.dot(X_r.T).dot(y)
e_r = y - X_r.dot(B_r)
rank_r = npl.matrix_rank(X_r)  # One column, rank 1
rank_r
# 1
# Calculate the F statistic
SSR_f = e_f.dot(e_f)
SSR_r = e_r.dot(e_r)
nu_1 = rank_f - rank_r
F = ((SSR_r - SSR_f) / nu_1) / (SSR_f / (n - rank_f))
F
# 3.66488...
