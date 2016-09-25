re_de_meaned = arr - means_expanded
# The row means are now very close to zero
re_de_meaned.mean(axis=1)
# array([  1.48029737e-16,   0.00000000e+00,   2.96059473e-16,
# 2.96059473e-16])
