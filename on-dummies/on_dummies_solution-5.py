#- Create design matrix for UCB / MIT ANOVA
Y = psychopathy
n = len(Y)
X = np.zeros((n, 2))
X[:5, 0] = 1  # UCB indicator
X[5:, 1] = 1  # MIT indicator
X
# array([[ 1.,  0.],
# [ 1.,  0.],
# [ 1.,  0.],
# [ 1.,  0.],
# [ 1.,  0.],
# [ 0.,  1.],
# [ 0.,  1.],
# [ 0.,  1.],
# [ 0.,  1.],
# [ 0.,  1.]])
