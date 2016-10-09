############################################
A worked example of the general linear model
############################################

See: `introduction to the general linear model`_.

Here we go through the matrix formulation of the GLM with the simplest
possible example |--| a t test for the difference of the sample mean from
zero.

Let us say we have the hypothesis that men are more psychopathic than women.

We find 10 male-female couples, and we give them each a psychopathy
questionnaire.  We score the questionnaires, and then, for each couple, we
subtract the woman's score from the man's score, to get a difference score.

We have 10 difference scores:

.. nbplot::

    >>> #: Our standard imports
    >>> import numpy as np
    >>> import numpy.linalg as npl
    >>> # Only show 4 decimals when printing arrays
    >>> np.set_printoptions(precision=4)

.. nbplot::

    >>> differences = np.array([ 1.5993, -0.13  ,  2.3806,  1.3761, -1.3595,
    ...                          1.0286,  0.8466,  1.6669, -0.8241,  0.4469])

Our hypothesis is that the females in the couple have a lower psychopathy
score, and therefore that, in the whole population of male-female couples,
this measure will, on average, be positive (men have higher scores than
women).

We teat this hypothesis by testing whether the sample mean is far enough from
0 that to make it unlikely that the population mean is actually 0.

******************************
The standard error of the mean
******************************

One way to test this, it to compare the mean value, to the `standard error of
the mean
<https://en.wikipedia.org/wiki/Standard_error#Standard_error_of_the_mean_2>`_.

As usual, define the *mean* of a vector of values $\vec{x}$ as:

.. math::

    \bar{x} = \frac{1}{n} \sum_{i=1}^n x_i

Define the *unviased estimate of the standard deviation* of $\vec{x}$ as:

.. math::

    s_x = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2}

Notice the $\frac{1}{n-1}$.   We have previously used $n$ rather than $n-1$ as
the divisor for the *sample stadnard deviation*.  Using $n$, our *sample
standard deviation* is a biased estimate of the population standard deviation.
Using $n-1$ as the divisor gives an unbiased estimate for population standard
deviation.

The standard error of the mean is:

.. math::

    SE_{\bar{x}} = \frac{s_x}{\sqrt{n}}

where $n$ is the number of samples, 10 in our case.

We can make a t statistic by dividing the mean by the standard error of the
mean:

.. math::

    t = \frac{\bar{x}}{SE_{\bar{x}}}

In our case:

.. nbplot::

    >>> x = differences
    >>> n = len(x)
    >>> x_bar = np.mean(x)
    >>> x_bar
    0.70314...
    >>> unviased_var_x = 1. / (n - 1) * np.sum((x - x_bar) ** 2)
    >>> s_x = np.sqrt(unviased_var_x)
    >>> s_x
    1.17718...
    >>> SEM = s_x / np.sqrt(n)
    >>> SEM
    0.37225...
    >>> t = x_bar / SEM
    >>> t
    1.88884...

**************************************
Testing using the general linear model
**************************************

It is overkill for us to use the general linear model for this, but it does
show how the machinery works in the simplest case.

:math:`\newcommand{Xmat}{\boldsymbol X} \newcommand{\bvec}{\vec{\beta}}`
:math:`\newcommand{\yvec}{\vec{y}} \newcommand{\xvec}{\vec{x}} \newcommand{\evec}{\vec{\varepsilon}}`

The matrix experssion of the general linear model is:

.. math::

   \yvec = \Xmat \bvec + \evec

:math:`\newcommand{Xmat}{\boldsymbol X} \newcommand{\bvec}{\vec{\beta}}`

Define our design matrix $\Xmat$ to have a single column of ones:

.. nbplot::

    >>> X = np.ones((n, 1))
    >>> X
    array([[ 1.],
           [ 1.],
           [ 1.],
           [ 1.],
           [ 1.],
           [ 1.],
           [ 1.],
           [ 1.],
           [ 1.],
           [ 1.]])

:math:`\newcommand{\bhat}{\hat{\bvec}} \newcommand{\yhat}{\hat{\yvec}}`

$\bhat$ is The least squares estimate for $\bvec$, and is given by:

.. math::

    \bhat = (\Xmat^T \Xmat)^{-1} \Xmat^T \yvec

Because $\Xmat$ is just a column of ones, $\Xmat^T \yvec = \sum_i{y_i}$.

$\Xmat^T \Xmat = n$, so $(\Xmat^T \Xmat)^{-1} = \frac{1}{n}$.

Thus:

.. math::

    \bhat = (\Xmat^T \Xmat)^{-1} \Xmat^T \yvec \\
    = \frac{1}{n} \sum_i{y_i} \\
    = \bar{y}

The student's t statistic from the general linear model is:

.. math::

   t = \frac{c^T \hat\beta}{\sqrt{\hat{\sigma}^2 c^T (\Xmat^T \Xmat)^+ c}}

where $\hat{\sigma}^2$ is our estimate of variance in the residuals, $c$ is a
contrast vector to select some combination of the desingn columns, and
$(\Xmat^T \Xmat)^+$ is the *pseudoinverse* of $\Xmat^T \Xmat$.

In our case we have only one design column, so $c = [1]$ and we can omit it.
$\hat{\sigma}^2 = s_x^2$ for $s_x$ defined above.  $\Xmat^T \Xmat$ is
invrtible, and we know the inverse already: $\frac{1}{n}$.  Therefore:

.. math::

   t = \frac{\bar{y}}{s_x \sqrt{\frac{1}{n}}} \\
   = \frac{\bar{x}}{SE_{\bar{x}}}
