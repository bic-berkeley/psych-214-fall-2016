#- Calculate (X.T X)^-1 X.T (the pseudoinverse)
piX = iXtX.dot(X.T)
piX.shape
# (2, 12)
