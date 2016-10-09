#- Create X design matrix fron column of ones and clammy vector
n = len(clammy)
X = np.ones((n, 2))
X[:, 1] = clammy
X
# array([[ 1.   ,  0.422],
# [ 1.   ,  0.406],
# [ 1.   ,  0.061],
# [ 1.   ,  0.962],
# [ 1.   ,  4.715],
# [ 1.   ,  1.398],
# [ 1.   ,  1.952],
# [ 1.   ,  5.095],
# [ 1.   ,  8.092],
# [ 1.   ,  5.685],
# [ 1.   ,  5.167],
# [ 1.   ,  7.257]])
