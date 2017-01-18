#######################################
Adding length 1 dimensions with newaxis
#######################################

NumPy has a nice shortcut for adding a length 1 dimension to an array.  It is
a little brain-bending, because it operates via array slicing:

.. nbplot::

    >>> import numpy as np

    >>> v = np.array([0, 3])
    >>> v.shape
    (2,)
    >>> # Insert a new length 1 dimension at the beginning
    >>> row_v = v[np.newaxis, :]
    >>> row_v.shape
    (1, 2)
    >>> row_v
    array([[0, 3]])
    >>> # Insert a new length 1 dimension at the end
    >>> col_v = v[:, np.newaxis]
    >>> col_v.shape
    (2, 1)
    >>> col_v
    array([[0],
           [3]])

Read this last slicing operation as "do slicing as normal, except, before
slicing, insert a length 1 dimension at the position of ``np.newaxis``".

In fact the name ``np.newaxis`` points to the familiar Python ``None`` object:

.. nbplot::

    >>> np.newaxis is None
    True

So, you also use the ``np.newaxis`` trick like this:

.. nbplot::

    >>> row_v = v[None, :]
    >>> row_v.shape
    (1, 2)
