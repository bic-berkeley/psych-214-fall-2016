#- Calculate fit of X_o to y_o
iXtX = npl.inv(X_o.T.dot(X_o))
B_o = iXtX.dot(X_o.T).dot(y_c)
B_o
# array([-0.    ,  0.8074])
