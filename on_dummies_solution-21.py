# Reduced design, and design matrix rank
X_r = X
rank_r = npl.matrix_rank(X_r)
rank_r
# 2
# Full design, and design matrix rank
X_f = np.column_stack((clammy, X))
rank_f = npl.matrix_rank(X_f)
rank_f
# 3
nu_1 = rank_f - rank_r
nu_1
# 1
