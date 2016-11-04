#- Calculate the degrees of freedom consumed by the design
m = npl.matrix_rank(X)
#- Calculate the degrees of freedom of the error
df_error = n - m
df_error
# 8
