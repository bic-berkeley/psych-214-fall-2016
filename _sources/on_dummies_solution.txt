.. vim: ft=rst

####################################
Modeling groups with dummy variables
####################################

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

We return to the psychopathy of students from Berkeley and MIT.

We get psychopathy questionnaire scores from another set of 5 students from
Berkeley:

.. nbplot::

    >>> #: Psychopathy scores from UCB students
    >>> ucb_psycho = np.array([2.9277, 9.7348, 12.1932, 12.2576, 5.4834])

We do the same for another set of 5 students from MIT:

.. nbplot::

    >>> #: Psychopathy scores from MIT students
    >>> mit_psycho = np.array([7.2937, 11.1465, 13.5204, 15.053, 12.6863])

Concatenate these into a ``psychopathy`` vector:

.. nbplot::

    >>> #: Concatenate UCB and MIT student scores
    >>> psychopathy = np.concatenate((ucb_psycho, mit_psycho))

We will use the general linear model to a two-level (UCB, MIT) single factor
(college) analysis of variance on these data.

Our model is that the Berkeley student data are drawn from some distribution
with a mean value that is characteristic for Berkeley: $y_i = \mu_{Berkeley} +
e_i$ where $i$ corresponds to a student from Berkeley.  There is also a
characteristic but possibly different mean value for MIT: $\mu_{MIT}$:

.. math::

    \newcommand{\yvec}{\vec{y}}
    \newcommand{\xvec}{\vec{x}}
    \newcommand{\evec}{\vec{\varepsilon}}
    \newcommand{Xmat}{\boldsymbol X}
    \newcommand{\bvec}{\vec{\beta}}
    \newcommand{\bhat}{\hat{\bvec}}
    \newcommand{\yhat}{\hat{\yvec}}

    y_i = \mu_{Berkeley} + e_i  \space\mbox{if}\space 1 \le i \le 5

    y_i = \mu_{MIT} + e_i \space\mbox{if}\space 6 \le i \le 10

We saw in `introduction to the general linear model`_ that we can encode this
group membership with dummy variables.  There is one dummy variable for each
group.  The dummy variables are *indicator* variables, in that they have 1 in
the row corresponding to observations in the group, and zero elsewhere.

We will compile a design matrix $\Xmat$ and use the matrix formulation of the
general linear model to do estimation and testing:

.. math::

   \yvec = \Xmat \bvec + \evec

************
ANOVA design
************

Create the design matrix for this ANOVA, with dummy variables corresponding to the UCB and MIT student groups:

.. nbplot::

    >>> #- Create design matrix for UCB / MIT ANOVA
    >>> Y = psychopathy
    >>> n = len(Y)
    >>> X = np.zeros((n, 2))
    >>> X[:5, 0] = 1  # UCB indicator
    >>> X[5:, 1] = 1  # MIT indicator
    >>> X
    array([[ 1.,  0.],
           [ 1.,  0.],
           [ 1.,  0.],
           [ 1.,  0.],
           [ 1.,  0.],
           [ 0.,  1.],
           [ 0.,  1.],
           [ 0.,  1.],
           [ 0.,  1.],
           [ 0.,  1.]])

Remember that, when $\Xmat^T \Xmat$ is invertible, our least-squares parameter
estimates $\bhat$ are given by:

.. math::

    \bhat = (\Xmat^T \Xmat)^{-1} \Xmat^T \yvec

First calculate $\Xmat^T \Xmat$. Are the columns of this design orthogonal?

.. nbplot::

    >>> #- Calculate transpose of design with itself.
    >>> #- Are the design columns orthogonal?
    >>> X.T.dot(X)
    array([[ 5.,  0.],
           [ 0.,  5.]])

Calculate the inverse of $\Xmat^T \Xmat$.

.. nbplot::

    >>> #- Calculate inverse of transpose of design with itself.
    >>> iXtX = npl.inv(X.T.dot(X))
    >>> iXtX
    array([[ 0.2,  0. ],
           [ 0. ,  0.2]])

.. admonition:: Question

    What is the relationship of the values on the diagonal of $(\Xmat^T
    \Xmat)^{-1}$ and the number of values in each group?


    Answer: call the number of students in each group $q$.  The diagonals of
    $\Xmat^T \Xmat$ are, for each column $\vec{w}$: $\sum_i {w_i^2}$, which
    reduces to $q=5$, the number of ones in each column.  Because $\Xmat^T
    \Xmat$ is diagonal, the inverse is:

    .. math::

        (\Xmat^T \Xmat)^{-1} =
        \begin{bmatrix}
        \frac{1}{p} & 0 \\
        0 & \frac{1}{p} \\
        \end{bmatrix}

    The diagonal values in $(\Xmat^T \Xmat)^{-1}$ are therefore the reciprocal
    of the number of values in each group.


Now calculate the second half of $(\Xmat^T \Xmat)^{-1} \Xmat^T \yvec$:
$\vec{p} = \Xmat^T \yvec$.

.. nbplot::

    >>> #- Calculate transpose of design matrix multiplied by data
    >>> XtY = X.T.dot(Y)

.. admonition:: Question

    What is the relationship of each element in this
    vector to the values of ``ucb_psycho`` and ``mit_psycho``?


    Answer: The dot product of the dummy variables resolves to the sum of the
    values for which the dummy vector value is 1 (and therefore not 0).
    Therefore the values are the sums of the values in ``ucb_psycho`` and
    ``mit_psycho`` respectively:

    >>> XtY
    array([ 42.5967,  59.6999])
    >>> # The apparent difference is just in the display of the numbers
    >>> np.sum(Y[:5])
    42.5966999...
    >>> np.sum(Y[5:])
    59.6999


Now calculate $\bhat$ using $(\Xmat^T \Xmat)^{-1} \Xmat^T \yvec$:

.. nbplot::

    >>> #- Calculate beta vector
    >>> B = iXtX.dot(XtY)
    >>> B
    array([  8.5193,  11.94  ])

Compare this vector to the means of the values in ``ucb_psycho`` and
``mit_psycho``:

.. nbplot::

    >>> #- Compare beta vector to means of each group
    >>> ucb_psycho.mean()
    8.51933...
    >>> mit_psycho.mean()
    11.93998...

.. admonition:: Question

    Using your knowledge of the parts of $(\Xmat^T \Xmat)^{-1} \Xmat^T \yvec$,
    explain the relationship of the values in $\bhat$ to the means of
    ``ucb_psycho`` and ``mit_psycho``.


    We found that $\Xmat^T \yvec$ contains the sums for ``ucb_psych`` and
    ``mit_psycho`` respectively.  $(\Xmat^T \Xmat)^{-1}$ is diagonal with
    entries $\frac{1}{q}$ where $q = 5$ is the number of observations in each
    group.  Therefore the entries in $\bhat$ are:

    .. math::

        \frac{1}{q} \sum_i{v_i}

    for each vector $\vec{v}$ ``ucb_psycho``, ``mit_psycho``, which is also
    the formula for the mean.


*********************************
Hypothesis testing with contrasts
*********************************

Remember the student's t statistic from the general linear model [#col-vec]_:

.. math::

    \newcommand{\cvec}{\vec{c}}
    t = \frac{\cvec^T \bhat}
    {\sqrt{\hat{\sigma}^2 \cvec^T (\Xmat^T \Xmat)^+ \cvec}}

Let's consider the top half of the t statistic, $c^T \bhat$.

Our hypothesis is that the mean psychopathy score for MIT students,
$\mu_{MIT}$, is higher than the mean psychopathy score for Berkeley students,
$\mu_{Berkeley}$.  What contrast vector $\cvec$ do we need to apply to $\bhat$
to express the difference between these means?  Apply this contrast vector to
$\bhat$ to get the top half of the t statistic.

.. nbplot::

    >>> #- Contrast vector to express difference between UCB and MIT
    >>> #- Resulting value will be high and positive when MIT students have
    >>> #- higher psychopathy scores than UCB students
    >>> c = np.array([-1, 1])
    >>> top_of_t = c.dot(B)
    >>> top_of_t
    3.42064...

Now the bottom half of the t statistic.  Remember this is
$\sqrt{\hat{\sigma}^2 \cvec^T (\Xmat^T \Xmat)^+ \cvec}$.

First we generate $\hat{\sigma^2}$ from the residuals of the model.

Calculate the fitted values and the residuals given the $\bhat$ that you have
already.

.. nbplot::

    >>> #- Calculate the fitted and residual values
    >>> fitted = X.dot(B)
    >>> residuals = Y - fitted

We want an unbiased variance estimate for $\hat\sigma^2$.  See the `worked
example of GLM`_ page and the `unbiased variance estimate`_ section for
details.

The general rule is that we divide the sum of squares by $n - m$ where $m$ is
the number of *independent* columns in the design matrix.  Specifically, $m$
is the `matrix rank`_ of the design $\Xmat$.  $m$ can also be called the
*degrees of freedom of the design*.  $n - m$ is the *degrees of freedom of the
error* (see `unbiased variance estimate`_).

.. nbplot::

    >>> #- Calculate the degrees of freedom consumed by the design
    >>> m = npl.matrix_rank(X)
    >>> #- Calculated the degrees of freedom of the error
    >>> df_error = n - m
    >>> df_error
    8

Calculate the unbiased *variance* estimate $\hat{\sigma^2}$ by dividing the
sums of squares of the residuals by the degrees of freedom of the error.

.. nbplot::

    >>> #- Calculate the unbiased variance estimate
    >>> var_hat = np.sum(residuals ** 2) / df_error
    >>> var_hat
    13.04946...

Now the calculate second part of the t statistic denominator,  $\cvec^T (\Xmat^T
\Xmat)^+ \cvec$. You already know that $\Xmat^T \Xmat$ is invertible, and you
have its inverse above, so you can use the inverse instead of the more general
pseudo-inverse.

.. nbplot::

    >>> #- Calculate c (X.T X) c.T
    >>> c_iXtX_ct = c.dot(npl.inv(X.T.dot(X))).dot(c)
    >>> c_iXtX_ct
    0.40000...

.. admonition:: Question

    What is the relationship of $\cvec^T (\Xmat^T \Xmat)^{-1} \cvec$ to $p$
    |--| the number of observations in each group?


    Answer: we already know that:

    .. math::

        (\Xmat^T \Xmat)^{-1} =
        \begin{bmatrix}
        \frac{1}{p} & 0 \\
        0 & \frac{1}{p} \\
        \end{bmatrix}

    With contrast $c = [-1, 1]$ we get:

    .. math::

        \cvec^T (\Xmat^T \Xmat)^{-1} \cvec = \frac{2}{p}


Now, what is our t-value ? 

.. nbplot::

    >>> tstat = top_of_t / np.sqrt(var_hat*c.T.dot(iXtX).dot(c))
    >>> tstat
    1.49720...

Is this significant ? Use the ``stats`` module from ``scipy`` to create a
t-distribution with ``df_error`` (degrees of freedom of the error).  See the
``t_stat`` function in `introduction to the general linear model`_ for
inspiration:

.. nbplot::

    >>> #- Use scipy.stats to test if your t-test value is significant.
    >>> import scipy.stats as sst
    >>> tdistrib = sst.t(df_error)
    >>> # 1 - cumulative density function (P(x <= t)
    >>> 1. - tdistrib.cdf(tstat)
    0.08635...
    >>> # This is the same as the "survival function"
    >>> tdistrib.sf(tstat)
    0.08635...
 
.. admonition:: Question

    Now imagine your UCB and MIT groups are not of equal size.  The total
    number of students $n$ has not changed. Call $b$ the number of Berkeley
    students in the $n=10$, where $b \in [1, 2, ... 9]$.  Write the number of
    MIT students as $n - b$.  Using your reasoning for the case of equal group
    sizes above, derive a simple mathematical formula for the result of
    $\cvec^T (\Xmat^T \Xmat)^{-1} \cvec$ in terms of $b$ and $n$. $\cvec$ is
    the contrast you chose above.  If all other things remain equal, such as
    $n = 10$, the $\hat{\sigma^2}$ and $\cvec^T \bhat$, then which of the
    possible values of $b$ should you chose to give the largest value for your
    t statistic?


    Answer: we now have:

    .. math::

        (\Xmat^T \Xmat)^{-1} =
        \begin{bmatrix}
        \frac{1}{b} & 0 \\
        0 & \frac{1}{n-b} \\
        \end{bmatrix}

    With contrast $c = [-1, 1]$ we get:

    .. math::

        \cvec^T (\Xmat^T \Xmat)^{-1} \cvec = \frac{1}{b} + \frac{1}{n-b}

    To investigate, we make a Python function returning the result for a given
    ``b`` and ``n``, and evalulate for the possible values of ``b``:

    .. nbplot::

        >>> def two_group_ct_ixtx_c(b, n):
        ...    return 1. / b + 1. / (n - b)
        ...
        >>> two_group_ct_ixtx_c(np.arange(1, 10), 10)
        array([ 1.1111,  0.625 ,  0.4762,  0.4167,  0.4   ,  0.4167,  0.4762,
                0.625 ,  1.1111])

    We want $\cvec^T (\Xmat^T \Xmat)^{-1} \cvec$ to be small so that the t
    value will be large.  So, all other things being equal, $b = 5$ will give
    the largest t value.

    In general, for a fixed $n$, we get the largest t statistic (and greatest
    power) when comparing two groups of equal size.


***************************
Hypothesis testing: F-tests
***************************

Imagine we have also measured the clammy score for the Berkeley and MIT
students.

.. nbplot::

    >>> #: Clamminess of handshake for UCB and MIT students
    >>> clammy = np.array([2.6386, 9.6094, 8.3379, 6.2871, 7.2775, 2.4787,
    ...                    8.6037, 12.8713, 10.4906, 5.6766])

We want to test whether the clammy score is useful in explaining
the psychopathy data, over and above the students' college affiliation.

To do this, we will use an `F test <F tests_>`_.

An F-test compares a *full model* $\Xmat_f$ with a *reduced model* $\Xmat_r$.

In our case, $\Xmat_f$ is the model containing the ``clammy`` regressor, as
well as the two dummy columns for the UCB and MIT group means.

$\Xmat_r$ is our original model, that only contains the dummy columns for the
UCB and MIT group means.

We define $SSR(\Xmat_r)$ and $SSR(\Xmat_f)$ as in `hypothesis tests`_.
These are the Sums of Squares of the Residuals of the reduced and full model
respectively.

.. math::

    \bhat_r = \Xmat_r^+ \yvec \\
    \hat\evec_r = \yvec - \Xmat_r \bhat_r \\
    SSR(\Xmat_r) = \hat\evec_r^T \hat\evec_r \\

    \bhat_f = \Xmat_f^+ \yvec \\
    \hat\evec_f = \yvec - \Xmat_f \bhat_f \\
    SSR(\Xmat_f) = \hat\evec_f^T \hat\evec_f

You can calculate the F statistic for adding the ``clammy`` regressor, by
using these calculations and the formula for the F-test in `F tests`_.

.. admonition:: Question

    Make the alternative full model $\Xmat_f$. Compute the extra degrees of
    freedom consumed by the design |--| ${\nu_1}$.  Compute the extra sum of
    squares and the F statistic.


    Answer: Construct $\Xmat_f$; compute $\nu_1$:

    .. nbplot::

        >>> # Reduced design, and design matrix rank
        >>> X_r = X
        >>> rank_r = npl.matrix_rank(X_r)
        >>> rank_r
        2
        >>> # Full design, and design matrix rank
        >>> X_f = np.column_stack((clammy, X))
        >>> rank_f = npl.matrix_rank(X_f)
        >>> rank_f
        3
        >>> nu_1 = rank_f - rank_r
        >>> nu_1
        1

    Make a function to compute $\bhat, \textrm{SSR}(\Xmat), \nu_2$ for a
    given $\Xmat$ and $\yvec$:

    .. nbplot::

        >>> def glm(X, Y):
        ...     """ Compute GLM on design `X` and data `Y`
        ...
        ...     Parameters
        ...     ----------
        ...     X : ndarray ahdpe (n, p)
        ...         design matrix, n observations by p columns.
        ...     Y : ndarray shape (n,) or (n,1)
        ...         data.
        ...
        ...     Returns
        ...     -------
        ...     beta : ndarray shape (p,)
        ...        estimated parameters for model `X`
        ...     residual_ss : float
        ...        sum of squares of residuals
        ...     df_error : float
        ...         Degrees of freedom due to error.
        ...     """
        ...     B = npl.pinv(X).dot(Y)
        ...     resid = Y - X.dot(B)
        ...     df = X.shape[0] - npl.matrix_rank(X)
        ...     return B, resid.T.dot(resid), df

    Compute F statistic:

    .. nbplot::

        >>> b_f, rss_f, df_f = glm(X_f, Y)
        >>> b_r, rss_r, df_r = glm(X_r, Y)
        >>> f_stat = ((rss_r - rss_f) / nu_1) / (rss_f / df_f)
        >>> f_stat
        6.15949...


.. rubric:: Footnotes

.. [#col-vec] Assume the default that for any $\vec{v}$, $\vec{v}$ is a
   column vector, and therefore that $\vec{v}^T$ is a row vector.
