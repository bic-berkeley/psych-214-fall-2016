#- Calculate inverse of transpose of design with itself.
iXtX = npl.inv(X.T.dot(X))
iXtX
# array([[ 0.2,  0. ],
# [ 0. ,  0.2]])
