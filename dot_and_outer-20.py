re_de_meaned = arr - means_expanded
# The row means are now very close to zero
re_de_meaned.mean(axis=1)
# array([ 0.,  0.,  0.,  0.])
