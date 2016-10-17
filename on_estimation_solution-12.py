#- Make second column orthogonal to first. Confirm orthogonality
X_o[:, 1] = X_o[:, 1] - X_o[:, 1].mean()
X_o.T.dot(X_o)
# array([[ 12.    ,   0.    ],
# [  0.    ,  90.8529]])
