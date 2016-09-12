######################################
Reshaping and three-dimensional arrays
######################################

Here is a one-dimensional array:

.. nbplot::

    >>> import numpy as np
    >>> arr_1d = np.arange(6)
    >>> arr_1d
    array([0, 1, 2, 3, 4, 5])
    >>> arr_1d.shape
    (6,)

We can reshape this array to two dimensions using the ``reshape`` method of
the array:

.. nbplot::

    >>> arr_2d = arr_1d.reshape((2, 3))
    >>> arr_2d
    array([[0, 1, 2],
           [3, 4, 5]])

Notice how NumPy used the 1D array elements.  It takes each element from the
1D array, and fills the rows first, and then the columns.

We can reshape back to one dimension.

.. nbplot::

    >>> arr_2d.reshape((6,))
    array([0, 1, 2, 3, 4, 5])

Here NumPy fetches the data from the rows first, and the columns, to fill out
the elements of the 1D array.

The value ``-1`` is special for the ``reshape`` method.  It means, "make a
dimension the size that will use the remaining unspecified elements".   We'll
see what "unspecified" means soon.  At the moment, "unspecified" is true of
all the elements, so the shape is the same as the number of elements in the 2D
array:

.. nbplot::

    >>> arr_2d.reshape(-1)
    array([0, 1, 2, 3, 4, 5])

It is very common to convert a 2 or 3 or N-dimensional array to a 1D array, so
there is a short-cut command for that:

.. nbplot::

    >>> arr_2d.ravel()
    array([0, 1, 2, 3, 4, 5])

You can reshape from one shape, to any other shape, as long as the number of
elements stays the same.  Can you see the algorithm NumPy is using to decide
which elements go in which position of the array?

.. nbplot::

    >>> arr_1d.reshape((3, 2))
    array([[0, 1],
           [2, 3],
           [4, 5]])

Reshape uses `-1` as a value to mean the shape value that will use the
remaining unspecified elements.  For example, we could specify that we want
the first dimension to be length 3, and NumPy can work out the second
dimension must be length 2, and the other way round:

.. nbplot::

    >>> arr_1d.reshape((3, -1))
    array([[0, 1],
           [2, 3],
           [4, 5]])
    >>> arr_1d.reshape((-1, 2))
    array([[0, 1],
           [2, 3],
           [4, 5]])

NumPy uses the same algorithm for reshaping a three-dimensional array:

.. nbplot::

    >>> arr_1d_bigger = np.arange(24)
    >>> arr_1d_bigger
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23])
    >>> arr_1d_bigger.shape
    (24,)
    >>> arr_3d = arr_1d_bigger.reshape((2, 3, 4))
    >>> arr_3d
    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    <BLANKLINE>
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])

Here NumPy is showing us the two slices over the first dimension:

.. nbplot::

    >>> arr_3d[0, :, :]
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])
    >>> arr_3d[1, :, :]
    array([[12, 13, 14, 15],
           [16, 17, 18, 19],
           [20, 21, 22, 23]])

To think about what array this is, imagine tipping the bottom of each 2D array
backwards from the screen, so 0 sits nearly on top of 12, in the plane of the
screen, and 1 sits nearly on top of 13.

Here are the two planes of the array (slices over the third dimension):

.. nbplot::

    >>> for i in range(3):
    ...     print(arr_3d[:, :, i])
    ...
    [[ 0  4  8]
     [12 16 20]]
    [[ 1  5  9]
     [13 17 21]]
    [[ 2  6 10]
     [14 18 22]]

We can reshape to one dimension in the same way as we did for the 2D arrays.

.. nbplot::

    >>> arr_3d.reshape(24)
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23])
    >>> arr_3d.reshape(-1)
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23])
    >>> arr_3d.ravel()
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23])

To get the elements of the 1D array, NumPy first fetches values across the
last axis (the depth or plane axis), then the second to last (column) axis,
then the first (row) axis.

When reshaping to three dimensions, NumPy fills out the last, then second,
then first dimensions:

.. nbplot::

    >>> arr_3d = arr_1d_bigger.reshape((2, 3, 4))
    >>> arr_3d
    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    <BLANKLINE>
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])
