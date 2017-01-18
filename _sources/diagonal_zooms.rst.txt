###############################################
Encoding zooms (scaling) with a diagonal matrix
###############################################

If I want to express the fact that I am expanding or contracting a coordinate
along the x axis, then I multiply the x coordinate by some scalar :math:`p`:

.. math::

    \begin{bmatrix}
    x'\\
    y'\\
    z'\\
    \end{bmatrix} =
    \begin{bmatrix}
    p x\\
    y\\
    z\\
    \end{bmatrix}

In general if I want to scale by :math:`p` in :math:`x`, :math:`q` in
:math:`y` and :math:`r` in :math:`z`, then I could multiply each coordinate by
the respective scaling:

.. math::

    \begin{bmatrix}
    x'\\
    y'\\
    z'\\
    \end{bmatrix} =
    \begin{bmatrix}
    p x\\
    q y\\
    r z\\
    \end{bmatrix}

We can do the same thing by multiplying the coordinate by a matrix with the
scaling factors on the diagonal:

.. math::

    \begin{bmatrix}
    x'\\
    y'\\
    z'\\
    \end{bmatrix} =
    \begin{bmatrix}
    p x\\
    q y\\
    r z\\
    \end{bmatrix} =
    \begin{bmatrix}
    p & 0 & 0 \\
    0 & q & 0 \\
    0 & 0 & r \\
    \end{bmatrix}
    \begin{bmatrix}
    x\\
    y\\
    z\\
    \end{bmatrix}

You can make these zooming matrices with :doc:`np.diag <numpy_diag>`:

.. nbplot::

    >>> import numpy as np
    >>> zoom_mat = np.diag([3, 4, 5])
    >>> zoom_mat
    array([[3, 0, 0],
           [0, 4, 0],
           [0, 0, 5]])
