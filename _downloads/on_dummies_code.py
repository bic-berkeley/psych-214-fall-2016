""" Modeling groups with dummy variables
"""
#: Import numerical and plotting libraries
import numpy as np
# Print to four digits of precision
np.set_printoptions(precision=4, suppress=True)
import numpy.linalg as npl
import matplotlib.pyplot as plt

#: Psychopathy scores from UCB students
ucb_psycho = np.array([2.9277, 9.7348, 12.1932, 12.2576, 5.4834])

#: Psychopathy scores from MIT students
mit_psycho = np.array([7.2937, 11.1465, 13.5204, 15.053, 12.6863])

#: Concatenate UCB and MIT student scores
psychopathy = np.concatenate((ucb_psycho, mit_psycho))

#- Create design matrix for UCB / MIT ANOVA

#- Calculate transpose of design with itself.
#- Are the design columns orthogonal?

#- Calculate inverse of transpose of design with itself.


""" What is the relationship of the values on the diagonal of the inverse
of X.T.dot(X) and the number of values in each group?

"""


#- Calculate transpose of design matrix multiplied by data


"""
What is the relationship of each element in this
vector to the values of ``ucb_psycho`` and ``mit_psycho``?
"""


#- Calculate beta vector

#- Compare beta vector to means of each group


r""" Using your knowledge of the parts of (X.T X)^{-1} X y, explain the
relationship of the values in $\bhat$ to the means of of ``ucb_psycho``
and ``mit_psycho``.

"""


#- Contrast vector to express difference between UCB and MIT
#- Resulting value will be high and positive when MIT students have
#- higher psychopathy scores than UCB students

#- Calculate the fitted and residual values

#- Calculate the degrees of freedom consumed by the design
#- Calculated the degrees of freedom of the error

#- Calculate the unbiased variance estimate

#- Calculate c (X.T X) c.T


""" What is the relationship of ``c.dot(npl.inv(X.T.dot(X)).dot(cvec)`` to
``p`` - the number of observations in each group?
"""



#- Use scipy.stats to test if your t-test value is significant.


""" Now imagine your UCB and MIT groups are not of equal size.  The total
number of students ``n`` has not changed. Call ``b`` the number of
Berkeley students in the ``n=10``, where ``b in range(1, 10)``.  Write the
number of MIT students as ``n - b``.  Using your reasoning from the equal
group sizes case above, derive a simple mathematical formula for the
result of ``c.dot(npl.inv(X.T.dot(X)).dot(c)`` in terms of ``b`` and
``n``. ``c`` is the contrast vector you chose above.  If all other things
remain equal, such as the sigma estimate and the top half of the t
statistic, then what value of ``b`` should you chose to give the largest
value for your t statistic?
"""


#: Clamminess of handshake for UCB and MIT students
clammy = np.array([2.6386, 9.6094, 8.3379, 6.2871, 7.2775, 2.4787,
                   8.6037, 12.8713, 10.4906, 5.6766])


"""
Make the alternative full model X_f. Compute the extra degrees of
freedom nu_1.  Compute the extra sum of squares and the F statistic.
"""

