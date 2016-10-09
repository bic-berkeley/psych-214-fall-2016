""" Understanding least-squares regression
"""
#: Import numerical and plotting libraries
import numpy as np
# Print to four digits of precision
np.set_printoptions(precision=4, suppress=True)
import numpy.linalg as npl
import matplotlib.pyplot as plt



#- Create X design matrix fron column of ones and clammy vector

#- Check whether the columns of X are orthogonal

#- Check whether X.T X is invertible

#- Calculate (X.T X)^-1 X.T (the pseudoinverse)

#- Calculate least squares fit for beta vector

#- Calculate the fitted values

#- mean of residuals near zero

#- Residuals orthogonal to design

#- Copy X to new array X_o

#- Make second column orthononal to first. Confirm orthogonality


""" What is the relationship between the values on the diagonal of
X_o.T.dot(X_o) and the lengths of the vectors in the first and second
columns of X_o?

"""



""" What is the relationship between the values on the diagonal of the
*inverse* of X_o.T.dot(X_o) and the lengths of the vectors in the first
and second columns of X_o?

"""


#- Make mean-centered version of psychopathy vector

#- Calculate fit of X_o to y_o


""" Explain the new value of the first element of the parameter estimate
vector.

"""


#- Correlation coefficient of y_c and the second column of X_o


""" What is the relationship between the correlation coefficient "r_xy"
and the second element in the parameter vector "B_o[1]"?

"""


#- Fit X_o to psychopathy data



""" Explain the relationship between the mean of the psychopathy values
and the first element of the parameter estimate vector.

"""



""" Why is the second value in B_o the same when estimating against "y_c"
and "psychopathy"?
"""


