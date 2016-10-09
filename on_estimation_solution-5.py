#- Check whether X.T X is invertible
iXtX = npl.inv(X.T.dot(X))  # No error in inversion
