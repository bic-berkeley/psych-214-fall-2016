# 1D vector is row vector on the left hand side of dot
v.dot(X)
# array([ 9, 12, 15])

# 1D vector is column vector on the right hand side of dot
w = np.array([-1, 0, 1])
X.dot(w)
# array([2, 2])
