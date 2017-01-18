#################
Diagonal matrices
#################

We often want to make matrices with all zeros except on the diagonal |--|
diagonal matrices.

Numpy does not fail us:

.. nbplot::

    >>> import numpy as np
    >>> np.diag([3, 4, 5, 6])
    array([[3, 0, 0, 0],
           [0, 4, 0, 0],
           [0, 0, 5, 0],
           [0, 0, 0, 6]])

.. nbplot::

    >>> np.diag([7, 8, 9, 10, 11])
    array([[ 7,  0,  0,  0,  0],
           [ 0,  8,  0,  0,  0],
           [ 0,  0,  9,  0,  0],
           [ 0,  0,  0, 10,  0],
           [ 0,  0,  0,  0, 11]])
