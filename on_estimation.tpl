.. vim: ft=rst

######################################
Understanding least-squares regression
######################################

****************************
Introduction and definitions
****************************

.. nbplot::

    >>> #: Import numerical and plotting libraries
    >>> import numpy as np
    >>> # Print to four digits of precision
    >>> np.set_printoptions(precision=4, suppress=True)
    >>> import numpy.linalg as npl
    >>> import matplotlib.pyplot as plt

These exercises are to practice thinking about how the regression estimation
works, and the relationship of correlation and regression.

To give us some concrete data to play with, here are some more samples of the
"psychopathy" and "clamminess" scores that we saw in the `introduction to the
general linear model`_:

.. nbplot::

    >>> psychopathy = [ 11.914,   4.289,  10.825,  14.987,   7.572,   5.447,
    ...                 17.332, 12.105,  13.297,  10.635,  21.777,  20.715])

    >>> clammy = [ 0.422,  0.406,  0.061,  0.962,  4.715,  1.398,  1.952,  5.095,
    ...            8.092,  5.685,  5.167,  7.257]

:math:`\newcommand{\yvec}{\vec{y}} \newcommand{\xvec}{\vec{x}} \newcommand{\evec}{\vec{\varepsilon}}`

Our simple linear model can be expressed by:

.. math::

    y_i = c + bx_i + e_i`

or, in vector notation:

.. math::

    \yvec = c + b \xvec + \evec

where $\yvec$ is the vector of values $[y_1, y_2, ... y_n]$ we want to explain
(psychopathy), $\xvec$ is the vector of values $[x_1, x_2, ... x_n]$
containing our explanatory variable (clammy), and $\evec$ is the vector of
remaining data unexplained by $c + b \xvec$.

:math:`\newcommand{Xmat}{\boldsymbol X} \newcommand{\bvec}{\vec{\beta}}`

The same model can also be expressed using a design *matrix* $\Xmat$:

.. math::

   \yvec = \Xmat \bvec + \evec

where $\Xmat$ has two columns, the first being a length $n$ vector of ones,
and the second being $\xvec$. $\bvec$ is column vector containing two values,
$[c, b]$ that are the intercept and slope of the fitted line.

Now define the *mean* of $\vec{x}$ as:

.. math::

    \bar{x} = \frac{1}{n} \sum_{i=1}^n x_i

Define two new vectors, $\vec{x^c}, \vec{y^c}$ that contain the values in
$\vec{x}, \vec{y}$ with their respective means subtracted:

.. math::

    \vec{x^c} = [x_1 - \bar{x}, x_2 - \bar{x}, ... , x_n - \bar{x}]

    \vec{y^c} = [y_1 - \bar{y}, y_2 - \bar{y}, ... , y_n - \bar{y}]

Define the *standard deviation* of $\vec{x}$ as:

.. math::

    s_x = \sqrt{\frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2}

From the the vector algebra in `vectors and dot products`_, $s^x$ is also
given by:

.. math::

    s_x = \sqrt{\frac{1}{n}} \; \; \VL{x^c}

See: `correlation and projection`_ for details.

We found in `introduction to the general linear model`_ that, for the case of
a full-rank matrix $\Xmat$, the least squares estimate for $\bvec$ is given
by:

.. math::

    \newcommand{\bhat}{\hat{\bvec}} \newcommand{\yhat}{\hat{\yvec}}
    \bhat = (\Xmat^T \Xmat)^{-1} \Xmat^T \yvec

**************************************
Correlation coefficient and regression
**************************************

Create the $\Xmat$ matrix from a vector of ones and the vector of ``clammy``
scores:

.. nplot::

    >>> #- Create X design matrix fron column of ones and clammy vector
    >>> n = length(clammy)
    >>> X = np.ones((n, 2))
    >>> X[:, 1] = clammy
    >>> X

Is $\Xmat^T \Xmat$ invertible?

.. nplot::

    >>> #- Check whether X.T X is invertible
    >>> iXtX = npl.inv(X.T.dot(X))  # No error in inversion

Calculate $(\Xmat^T \Xmat)^{-1} \Xmat^T$.  What shape is it?

.. nplot::

    >>> #- Calculate pseudoinverse of (X.T X)^-1 X.T
    >>> piX = iXtX.dot(X.T)
    >>> piX.shape

Calculate the least squares fit value for $\bvec$:

.. nplot::

    >>> #- Calculate least squares fit for beta vector
    >>> B = piX.dot(psychopathy)
    B

.. solution-start

Here's a solution

.. solution-replace

Here's a question

.. solution-end

More text

.. solution-start

Here's another solution

.. solution-end

More text still
