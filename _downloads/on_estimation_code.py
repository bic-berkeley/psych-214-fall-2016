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

#- Make mean-centered version of psychopathy vector

#- Calculate fit of X_o to y_o

#- Correlation coefficient of y_c and the second column of X_o

#- Fit X_o to psychopathy data

