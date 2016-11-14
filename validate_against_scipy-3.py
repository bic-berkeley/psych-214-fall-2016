X = np.ones((n, 2))
X[:, 1] = x
B = npl.pinv(X).dot(y)
B
# array([ 19.3567,   0.0723])
E = y - X.dot(B)
