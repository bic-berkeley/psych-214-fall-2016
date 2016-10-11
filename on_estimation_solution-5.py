#- Check whether X.T.dot(X) is invertible
iXtX = npl.inv(X.T.dot(X))  # No error in inversion
