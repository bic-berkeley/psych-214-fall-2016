####################################
``numpy.tranpose`` for swapping axes
####################################

Numpy allows you to swap axes without costing anything in memory, and very
little in time.

The obvious axis swap is a 2D array transpose:

.. nbplot::

    >>> import numpy as np
    >>> arr = np.arange(10).reshape((5, 2))
    >>> arr
    array([[0, 1],
           [2, 3],
           [4, 5],
           [6, 7],
           [8, 9]])

.. nbplot::

    >>> arr.T
    array([[0, 2, 4, 6, 8],
           [1, 3, 5, 7, 9]])

The ``transpose`` method - and the ``np.tranpose`` function does the same
thing as the ``.T`` attribute above:

.. nbplot::

    >>> arr.transpose()
    array([[0, 2, 4, 6, 8],
           [1, 3, 5, 7, 9]])

The advantage of ``transpose`` over the ``.T`` attribute is that is allows you
to move axes into any arbitrary order.

For example, let's say you had a 3D array:

.. nbplot::

    >>> arr = np.arange(24).reshape((2, 3, 4))
    >>> arr
    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    <BLANKLINE>
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])

.. nbplot::

    >>> arr.shape
    (2, 3, 4)

.. nbplot::

    >>> arr[:, :, 0]
    array([[ 0,  4,  8],
           [12, 16, 20]])

``transpose`` allows you to re-order these axes as you like. For example,
maybe you wanted to take the current last axis, and make it the first axis.
You pass ``transpose`` the order of the axes that you want:

.. nbplot::

    >>> new_arr = arr.transpose(2, 0, 1)

.. nbplot::

    >>> new_arr
    array([[[ 0,  4,  8],
            [12, 16, 20]],
    <BLANKLINE>
           [[ 1,  5,  9],
            [13, 17, 21]],
    <BLANKLINE>
           [[ 2,  6, 10],
            [14, 18, 22]],
    <BLANKLINE>
           [[ 3,  7, 11],
            [15, 19, 23]]])

.. nbplot::

    >>> new_arr.shape
    (4, 2, 3)

.. nbplot::

    >>> new_arr[0, :, :]
    array([[ 0,  4,  8],
           [12, 16, 20]])

Notice that the contents of the axis has not changed, just the position.
``new_arr[i, :, :]`` is the same as ``arr[:, :, i]`` for any ``i``.
