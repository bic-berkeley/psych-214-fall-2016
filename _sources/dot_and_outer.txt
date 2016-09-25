#######################################################
Numpy functions; more on reshape; arange, dot and outer
#######################################################

.. nbplot::
    :include-source: false

    >>> # - compatibility with Python 2
    >>> from __future__ import print_function
    >>> from __future__ import division
    >>> # - import common modules
    >>> import numpy as np  # the Python array package
    >>> import matplotlib.pyplot as plt  # the Python plotting package

*****************************
Methods vs functions in numpy
*****************************

Many things are implemented in numpy as both *functions* and *methods*.  For
example, there is a ``np.sum`` function, that adds up all the elements:

.. nbplot::

    >>> arr = np.array([1, 2, 0, 1])
    >>> np.sum(arr)
    4

There is also a ``sum`` method of the numpy ``array`` object:

.. nbplot::

    >>> type(arr)
    <class 'numpy.ndarray'>

.. nbplot::

    >>> arr.sum()
    4

Nearly all the method versions do the same thing as the function versions.
Examples are ``mean``, ``min``, ``max``, ``sum``, ``reshape``.  Choosing the
method or the function will usually depend on which one is easier to read.

***************
More on reshape
***************

The obvious example - making an array flat (1D):

.. nbplot::

    >>> arr = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
    >>> arr
    array([[ 0,  1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10, 11]])

.. nbplot::

    >>> arr_1d = arr.reshape(12)
    >>> arr_1d
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

Notice what happened. Numpy first makes an output array shape ``(12,)``.
It then proceeds along the *last* axis, element by element, taking the
element and putting it into the output array. When it has finished each
line on the last axis, it continues to the next line (on the
second-to-last axis).

We can reverse the process, like this:

.. nbplot::

    >>> arr_1d.reshape((2, 6))
    array([[ 0,  1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10, 11]])

Making an N-D array into a 1D array is very common, so numpy has a
short-cut for that:

.. nbplot::

    >>> arr.ravel()
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

For a 3D array, there are three axes. In this case numpy first proceeds
along the lines over the third axis. When it reaches the end of the line
it moves to the next line on the *second* axis, and when it gets to the
end of the second axis it goes to the first axis.

.. nbplot::

    >>> arr_3d = np.array([ # now define first of 2 2D arrays (arr_3d[0, :, :])
    ...                     [[0,  1,  2,  3],
    ...                      [4,  5,  6,  7],
    ...                      [8,  9, 10, 11]],
    ...                     # define second of 2 2D arrays (arr_3d[1, :, :])
    ...                     [[12, 13, 14, 15],
    ...                      [16, 17, 18, 19],
    ...                      [20, 21, 22, 23]]
    ...                   ])
    >>> arr_3d
    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])

.. nbplot::

    >>> n_elements = 2 * 3 * 4
    >>> arr_3d.reshape(n_elements)
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23])

You can reshape to any shape. For example, you might want to reshape
only the first two dimensions, leaving the last the same. This will take
you from an array of shape (2, 3, 4), to an array of shape (6, 4). The
procedure is the same in numpy. It makes an output array shape (6, 4),
then takes each element over the last dimension in the input, and fills
the last dimension of the output, moves one across on the second
dimension of the input, then fills a line in the first dimension of the
output, and so on.

.. nbplot::

    >>> arr_2d = arr_3d.reshape(6, 4)
    >>> arr_2d.shape
    (6, 4)

.. nbplot::

    >>> arr_2d
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15],
           [16, 17, 18, 19],
           [20, 21, 22, 23]])

Of course we can do this with image data arrays:

.. nbplot::

    >>> import nibabel as nib
    >>> img = nib.load('ds114_sub009_t2r1.nii')
    >>> data = img.get_data()
    >>> data.shape
    (64, 64, 30, 173)

.. nbplot::

    >>> vol_shape = data.shape[:-1]
    >>> vol_shape
    (64, 64, 30)

Here I am using the ``np.prod`` function, which is like ``np.sum``, but
instead of adding the elements, it multiplies them:

.. nbplot::

    >>> n_voxels = np.prod(vol_shape)
    >>> n_voxels
    122880

.. nbplot::

    >>> voxel_by_time = data.reshape(n_voxels, data.shape[-1])
    >>> voxel_by_time.shape
    (122880, 173)

The outer product
=================

We can use the rules of matrix multiplication for row vectors and column
vectors.

A row vector is a 2D vector where the first dimension is length 1.

.. nbplot::

    >>> row_vector = np.array([[1, 3, 2]])
    >>> row_vector
    array([[1, 3, 2]])

A column vector is a 2D vector where the second dimension is length 1.

.. nbplot::

    >>> col_vector = np.array([[2], [0], [1]])
    >>> col_vector
    array([[2],
           [0],
           [1]])

We know what will happen if we matrix multiply the row vector and the
column vector:

.. nbplot::

    >>> row_vector.dot(col_vector)
    array([[4]])

What happens with we matrix multiply the column vector by the row
vector? We know this will work because we are multiplying a 3 by 1 array
by a 1 by 3 array, so this should generate a 3 by 3 array:

.. nbplot::

    >>> col_vector.dot(row_vector)
    array([[2, 6, 4],
           [0, 0, 0],
           [1, 3, 2]])

This arises from the rules of matrix multiplication, except there is
only one row \* value pair for each dot product making up the rows and
columns:

.. nbplot::

    >>> print(col_vector[0] * row_vector)
    >>> print(col_vector[1] * row_vector)
    >>> print(col_vector[2] * row_vector)

    [[2 6 4]]
    [[0 0 0]]
    [[1 3 2]]

This (M by 1) vector matrix multiply with a (1 by N) vector is also
called the *outer product* of two vectors. We can generate the same
thing from 1D vectors, by using the numpy ``np.outer`` function:

.. nbplot::

    >>> np.outer(col_vector.ravel(), row_vector.ravel())
    array([[2, 6, 4],
           [0, 0, 0],
           [1, 3, 2]])

Subtracting the mean
====================

We often want to do operations like subtract the mean from the columns
or rows of a 2D array. For example, here is a 4 by 3 array:

.. nbplot::

    >>> arr = np.array([[3., 1, 4], [1, 5, 9], [2, 6, 5], [3, 5, 8]])
    >>> arr
    array([[ 3.,  1.,  4.],
           [ 1.,  5.,  9.],
           [ 2.,  6.,  5.],
           [ 3.,  5.,  8.]])

Let's say I wanted to remove the mean across the columns (the row mean).
Here is the row mean:

.. nbplot::

    >>> row_means = np.mean(arr, axis=1)  # mean across the second (column) axis
    >>> row_means
    array([ 2.66666667,  5.        ,  4.33333333,  5.33333333])

This is a 1D array:

.. nbplot::

    >>> row_means.shape
    (4,)

I want do something like the following, but in a neater and faster way:

.. nbplot::

    >>> de_meaned = arr.copy()
    >>> for i in range(arr.shape[0]):  # iterate over rows
    ...     de_meaned[i] = de_meaned[i] - row_means[i]
    >>> # The rows now have very near 0 mean
    >>> de_meaned.mean(axis=1)
    array([  1.48029737e-16,   0.00000000e+00,   2.96059473e-16,
             2.96059473e-16])

One way of doing this, is expanding 1D shape (4,) mean vector out to a
shape (3, 4) array, where the new columns are all the same as the (4,)
mean vector. In fact you can do this with ``np.outer`` and a vector of
ones:

.. nbplot::

    >>> means_expanded = np.outer(row_means, np.ones(3))
    >>> means_expanded
    array([[ 2.66666667,  2.66666667,  2.66666667],
           [ 5.        ,  5.        ,  5.        ],
           [ 4.33333333,  4.33333333,  4.33333333],
           [ 5.33333333,  5.33333333,  5.33333333]])

Now we can subtract this expanded array to remove the row means:

.. nbplot::

    >>> re_de_meaned = arr - means_expanded
    >>> # The row means are now very close to zero
    >>> re_de_meaned.mean(axis=1)
    array([  1.48029737e-16,   0.00000000e+00,   2.96059473e-16,
             2.96059473e-16])

This is an example of *vectorizing*. We worked out a way of doing the
operation we wanted by using arrays, rather than having to loop over the
rows of the matrix.

We'll see later that there are even neater ways to do this, using a
technique called *broadcasting*.

Subplots and axes
=================

We often want to do several plots on the same figure.

We've already seen examples of doing this with the matplotlib
``subplots`` command.

The standard input arguments to ``subplots`` are the number of rows and
the number of columns you want in your grid of axes. For example, if you
want two plots underneath each other you would call ``subplots(2, 1)``
for two rows and one column.

``subplots`` returns a ``figure`` object, that is an object representing
the figure containing the axes. It also returns a list of ``axes``. The
axes are objects represting the axes on which we can plot. The axis
objects have methods like ``plot`` and ``imshow`` that allow us to plot
on the given axes:

.. nbplot::

    >>> x = np.arange(0, np.pi * 2, 0.1)
    >>> fig, axes = plt.subplots(2, 1)
    >>> axes[0].plot(x, np.sin(x))
    >>> axes[1].plot(x, np.cos(x))
    [...]

.. Also:

    plotting lines

