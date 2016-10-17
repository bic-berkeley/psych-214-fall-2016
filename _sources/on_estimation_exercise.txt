######################################
Understanding least-squares regression
######################################

* For code template see: :download:`on_estimation_code.py`;
* For solution see: :doc:`on_estimation_solution`.

.. vim: ft=rst


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

    >>> #: The data, that we are trying to model.
    >>> psychopathy = np.array([ 11.914,   4.289,  10.825,  14.987,
    ...                          7.572,   5.447,   17.332,  12.105,
    ...                          13.297,  10.635,  21.777,  20.715])

    >>> #: The regressor that we will use to model the data.
    >>> clammy = np.array([ 0.422,  0.406,  0.061,  0.962,  4.715,
    ...                     1.398,  1.952,  5.095, 8.092,  5.685,
    ...                     5.167,  7.257])

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

.. nbplot::

    >>> #- Create X design matrix fron column of ones and clammy vector

Are the columns of ``X`` orthogonal to each other?

.. nbplot::

    >>> #- Check whether the columns of X are orthogonal

Is $\Xmat^T \Xmat$ invertible?

.. nbplot::

    >>> #- Check whether X.T.dot(X) is invertible

Calculate $(\Xmat^T \Xmat)^{-1} \Xmat^T$.  What shape is it?

.. nbplot::

    >>> #- Calculate (X.T X)^-1 X.T (the pseudoinverse)

Calculate the least squares fit value for $\bvec$:

.. nbplot::

    >>> #- Calculate least squares fit for beta vector

Calculate the fitted values $c + b \xvec$, and the residuals $\evec$:

.. nbplot::

    >>> #- Calculate the fitted values

Confirm that the mean of the residuals is close to zero:

.. nbplot::

    >>> #- mean of residuals near zero

Confirm that residuals are orthogonal to both columns of the design matrix:

.. nbplot::

    >>> #- Residuals orthogonal to design

We will not modify the design to see what happens to the parameters and the
fitted values.

To keep our calculations for the original and new designs, start by copying
``X`` to make a new array ``X_o``.  Hint: tab complete on the array object in
IPython.

.. nbplot::

    >>> #- Copy X to new array X_o

We found that above that the columns of ``X`` are not orthogonal.  How can we
modify the second column of ``X`` to make it orthogonal to the first?  Hint:
write out the dot product of the first column with the second as a sum, and
simplify. Use that result to work out what to subtract from the second column
so the dot product is 0.

.. nbplot::

    >>> #- Make second column orthogonal to first. Confirm orthogonality


Look at the diagonal values of the matrix ``X_o.T.dot(X_o)``.  What is the
relationship of these values to the lengths of the vectors in the first and
second columns of ``X_o``?

.. admonition:: Answer


    ?


Use ``numpy.linalg.inv`` to find $(\Xmat^T \Xmat)^{-1}$ |--| the inverse of
``X_o.T.dot(X_o)``. Now what is the relationship of the values in the diagonal
of the inverse matrix to the lengths of the vectors in the first and second
columns of ``X_o``?  Hint: $A^{-1} \cdot A = I$; if $A$ has all zeros off the
diagonal, what must $A^{-1}$ be for this to be true?

.. admonition:: Answer


    ?


Make a new data vector ``y_c`` by subtracting the mean from the psychopathy
vector:

.. nbplot::

    >>> #- Make mean-centered version of psychopathy vector

Calculate a new ``B_o`` parameter vector for the least-squares fit of ``X_o``
to ``y_c``:

.. nbplot::

    >>> #- Calculate fit of X_o to y_o

The first parameter has changed compared to your previous estimate.  Can you
explain its new value?

.. admonition:: Answer


    ?


Calculate the correlation coefficient between ``y_c`` and the second column of
``X_o``:

.. nbplot::

    >>> #- Correlation coefficient of y_c and the second column of X_o

What is the relationship between this correlation coefficient and ``B_o[1]``?
Hint: what is the relationship of the correlation coefficient to vector dot
products?  See: `correlation and projection`_ for a reminder.

.. admonition:: Answer


    ?


Now try calculating $\bvec$ fitting the ``X_o`` design to the original
psychopathy data (not the mean-centered version).

.. nbplot::

    >>> #- Fit X_o to psychopathy data

Compare the first value in the new ``B_o`` parameter vector with the mean of
the ``psychpathy`` vector.

.. nbplot::


Can you explain the relationship?

.. admonition:: Answer


    ?


For extra points, can you explain why the second value in ``B_o`` did not
change when we estimated for ``psychopathy`` rather than the mean-centered
version ``y_c``?  Hint: remember $(\vec{a} + \vec{b}) \cdot \vec{c} = \vec{a}
\cdot \vec{c} + \vec{b} \cdot \vec{c}$.

.. admonition:: Answer


    ?


Calculate the fitted values for the ``X_o`` model, and compare them to the
fitted values for the original model:

.. nbplot::


For even more extra points, explain the relationship between the fitted values
for the original model and those for the new model, where the clammy regressor
is mean centered.

.. admonition:: Answer


    ?

.. solution-code-replace:

    """ Explain the relationship between the fitted values for the original
    model and those for the new model, where the clammy regressor is mean
    centered.

    """

