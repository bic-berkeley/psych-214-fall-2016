#########################################
Subtracting the mean from columns or rows
#########################################

.. nbplot::
    :include-source: false

    >>> # - compatibility with Python 2
    >>> from __future__ import print_function
    >>> from __future__ import division

We often want to do operations like subtract the mean from the columns or rows
of a 2D array. For example, here is a 4 by 3 array:

.. nbplot::

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> # Display array values to 6 digits of precision
    >>> np.set_printoptions(precision=6, suppress=True)

.. nbplot::

    >>> arr = np.array([[3., 1, 4], [1, 5, 9], [2, 6, 5], [3, 5, 8]])
    >>> arr
    array([[ 3.,  1.,  4.],
           [ 1.,  5.,  9.],
           [ 2.,  6.,  5.],
           [ 3.,  5.,  8.]])

Let's say I wanted to remove the mean across the columns (the row mean).  Here
is the row mean:

.. nbplot::

    >>> # Mean across the second (column) axis
    >>> row_means = np.mean(arr, axis=1)
    >>> row_means
    array([ 2.666667,  5.      ,  4.333333,  5.333333])

This is a 1D array:

.. nbplot::

    >>> row_means.shape
    (4,)

I want do something like the following, but in a neater and faster way:

.. nbplot::

    >>> # Use a loop to subtract the mean from each row
    >>> de_meaned = arr.copy()
    >>> for i in range(arr.shape[0]):  # iterate over rows
    ...     de_meaned[i] = de_meaned[i] - row_means[i]
    >>> # The rows now have very near 0 mean
    >>> de_meaned.mean(axis=1)
    array([ 0.,  0.,  0.,  0.])

***********************************
An inefficient way using "np.outer"
***********************************

One way of doing this subtraction, is to expand the 1D shape (4,) mean vector
out to a shape (3, 4) array, where the new columns are all the same as the
(4,) mean vector.  In fact you can do this with ``np.outer`` and a vector of
ones:

.. nbplot::

    >>> means_expanded = np.outer(row_means, np.ones(3))
    >>> means_expanded
    array([[ 2.666667,  2.666667,  2.666667],
           [ 5.      ,  5.      ,  5.      ],
           [ 4.333333,  4.333333,  4.333333],
           [ 5.333333,  5.333333,  5.333333]])

Now we can subtract this expanded array to remove the row means:

.. nbplot::

    >>> re_de_meaned = arr - means_expanded
    >>> # The row means are now very close to zero
    >>> re_de_meaned.mean(axis=1)
    array([ 0.,  0.,  0.,  0.])

This is an example of *vectorizing*. We worked out a way of doing the
operation we wanted by using arrays, rather than having to loop over the rows
of the matrix.

*****************************************
An efficient way using NumPy broadcasting
*****************************************

Our example array is shape (4, 3):

.. nbplot::

    >>> arr.shape
    (4, 3)

Above we used ``np.outer`` to make a new array shape (4, 3) that replicates
the shape (4,) row mean values across 3 columns.  We then subtract the new (4,
3) mean array from the original to subtract the mean.

`NumPy broadcasting`_ is a way to get to the same outcome, but without
creating a new (4, 3) shaped array.  Although broadcasting takes a while to
get used to, it usually results in code that is more concise and saves memory
by avoiding large temporary arrays.  In our case, the temporary means array of
shape (4, 3) is very small, but if ``arr`` had many more rows and / or
columns, then the temporary means array could be very large.

See `NumPy broadcasting`_ for a detailed description of how broadcasting
works. Here, we can summarize by saying that broadcasting tries to guess what
full arrays we will need by replicating rows or columns or planes until the
shapes of the two input arrays match.

Here is the broadcasting way of subtracting the row means:

.. nbplot::

    >>> # Make row_means into column vector so numpy knows to replicate
    >>> # the columns during broadcasting.
    >>> row_means_col_vec = row_means.reshape((4, 1))  # Better: np.newaxis.
    >>> broadcast_demeaned = arr - row_means_col_vec
    >>> broadcast_demeaned.mean(axis=1)
    array([ 0.,  0.,  0.,  0.])

When NumPy sees ``arr - row_means_col_vec`` it notices that ``arr`` is shape
(4, 3) and ``row_mean_col_vec`` is shape (4, 1).  It can't do an elementwise
operation like subtract with these shapes, so it will try and work out if it
can expand any missing or length 1 dimensions in the input arrays to make the
shapes match.  In this case, it sees that it can replicate the column of
``row_mean_col_vec`` 3 times to make an array shape (4, 3).   It does this in
an efficient way that re-uses the memory from the first column to make up the
data for the other columns, therefore saving memory compared to creating a new
full (4, 3) array.

You can see what NumPy is going to do when it tries to do elementwise
operations on arrays of these shapes by using ``np.broadcast_arrays``:

.. nbplot::

    >>> # Show what arrays NumPy will broadcast to.
    >>> bc_arr, bc_row_means = np.broadcast_arrays(arr, row_means_col_vec)
    >>> # The (4, 3) array is unchanged when broadcasting.
    >>> np.all(bc_arr == arr)
    True
    >>> # The (4, 1) array has its columns replicated to give a (4, 3) array.
    >>> bc_row_means
    array([[ 2.666667,  2.666667,  2.666667],
           [ 5.      ,  5.      ,  5.      ],
           [ 4.333333,  4.333333,  4.333333],
           [ 5.333333,  5.333333,  5.333333]])
