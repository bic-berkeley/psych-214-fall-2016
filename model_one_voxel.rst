#######################
Modeling a single voxel
#######################

Earlier |--| :doc:`voxel_time_courses` |--| we were looking at a single voxel
time course.

Let's get that same voxel time course back again:

.. nbplot::

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> import nibabel as nib
    >>> # Only show 6 decimals when printing
    >>> np.set_printoptions(precision=6)

    >>> img = nib.load('ds114_sub009_t2r1.nii')
    >>> data = img.get_data()
    >>> data = data[..., 4:]

The voxel coordinate (3D coordinate) that we were looking at before was at
(42, 32, 19):

.. nbplot::

    >>> voxel_time_course = data[42, 32, 19]
    >>> plt.plot(voxel_time_course)
    [...]

Now we are going to use our new convolved regressor to do a simple regression
on this voxel time course.

If you don't have it already, you will need to download
:download:`ds114_sub009_t2r1_conv.txt`.

.. nbplot::

    >>> convolved = np.loadtxt('ds114_sub009_t2r1_conv.txt')
    >>> # Knock off first 4 elements to match data
    >>> convolved = convolved[4:]
    >>> plt.plot(convolved)
    [...]

First we make our *design matrix*.  It has a column for the convolved
regressor, and a column of ones:

.. nbplot::

    >>> N = len(convolved)
    >>> X = np.ones((N, 2))
    >>> X[:, 0] = convolved
    >>> plt.imshow(X, interpolation='nearest', cmap='gray', aspect=0.1)
    <...>

:math:`\newcommand{\yvec}{\vec{y}}`
:math:`\newcommand{\xvec}{\vec{x}}`
:math:`\newcommand{\evec}{\vec{\varepsilon}}`
:math:`\newcommand{Xmat}{\boldsymbol X} \newcommand{\bvec}{\vec{\beta}}`
:math:`\newcommand{\bhat}{\hat{\bvec}} \newcommand{\yhat}{\hat{\yvec}}`

As you will remember from the `introduction to the General Linear Model`_, our
model is:

.. math::

   \yvec = \Xmat \bvec + \evec

We can get our least squares parameter *estimates* for $\bvec$ with:

.. math::

   \bhat = \Xmat^+y

where $\Xmat^+$ is the *pseudoinverse* of $\Xmat$.  When $\Xmat$ is
invertible, the pseudoinverse is given by:

.. math::

    \Xmat^+ = (\Xmat^T \Xmat)^{-1} \Xmat^T

Let's calculate the pseudoinverse for our design:

.. nbplot::

    >>> import numpy.linalg as npl
    >>> Xp = npl.pinv(X)
    >>> Xp.shape
    (2, 169)

We calculate $\bhat$:

.. nbplot::

    >>> beta_hat = Xp.dot(voxel_time_course)
    >>> beta_hat
    array([   31.185514,  2029.367685])

We can then calculate $\yhat$ (also called the *fitted data*):

.. nbplot::

    >>> y_hat = X.dot(beta_hat)
    >>> e_vec = voxel_time_course - y_hat
    >>> print(np.sum(e_vec ** 2))
    41405.572776...
    >>> plt.plot(voxel_time_course)
    [...]
    >>> plt.plot(y_hat)
    [...]
