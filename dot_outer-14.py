# Turn 1D vector into explicit row vector
row_v = v.reshape((1, 2))
# Dot new returns a row vector rather than a 1D vector
row_v.dot(X)
# array([[ 9, 12, 15]])
