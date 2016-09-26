###############################################################
NumPy and Matplotlib: reshape, dot products, lines and subplots
###############################################################

.. nbplot::
    :include-source: false

    >>> # - compatibility with Python 2
    >>> from __future__ import print_function
    >>> from __future__ import division

Our standard imports to start:

.. nbplot::

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> # Display array values to 6 digits of precision
    >>> np.set_printoptions(precision=6, suppress=True)

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

We often find ourselves doing complicated reshape operations when we are
dealing with images.   For example, we may find ourselves reshaping the first
few dimensions, but leaving the last intact.

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
    <BLANKLINE>
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])

For example, we might want to reshape only the first two dimensions, leaving
the last the same. This will take us from an array of shape (2, 3, 4), to an
array of shape (6, 4). The procedure is the same for all reshapes in NumPy.
NumPy makes an output array shape (6, 4), then takes each element over the
last dimension in the input, and fills the last dimension of the output, moves
one across on the second dimension of the input, then fills a line in the
first dimension of the output, and so on.

.. nbplot::

    >>> arr_2d = arr_3d.reshape(6, 4)
    >>> arr_2d.shape
    (6, 4)
    >>> arr_2d
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15],
           [16, 17, 18, 19],
           [20, 21, 22, 23]])

It is a common to do this kind of operation on image data arrays.  Here we
have a 4D array from an FMRI run (:download:`ds114_sub009_t2r1.nii`):

.. nbplot::

    >>> import nibabel as nib
    >>> img = nib.load('ds114_sub009_t2r1.nii')
    >>> data = img.get_data()
    >>> data.shape
    (64, 64, 30, 173)

We can think of the 4D array as a sequence of 3D volumes:

.. nbplot::

    >>> vol_shape = data.shape[:-1]
    >>> vol_shape
    (64, 64, 30)

To get the number of voxels in the volume, we can use the ``np.prod``
function on the shape. ``np.prod`` is like ``np.sum``, but instead of adding
the elements, it multiplies them:

.. nbplot::

    >>> n_voxels = np.prod(vol_shape)
    >>> n_voxels
    122880

Then we can reshape the array to 2D, with voxels on the first axis, and time
(volume) on the second.

.. nbplot::

    >>> voxel_by_time = data.reshape(n_voxels, data.shape[-1])
    >>> voxel_by_time.shape
    (122880, 173)

This is a useful operation when we want to apply some processing on all
voxels, without regard to their relative spatial position.

********
allclose
********

When the computer calculates a floating point value, there will often be some
degree of error in the calculation, because the computer floating point format
cannot represent every floating point number exactly. See:

* `floating point`_;
* `floating point error`_.

When we check the results of a floating point calculation, we often want to
avoid checking if the returned value is exactly equal to a desired value.
Rather, we want to check whether the returned value is close enough, given the
usual floating point error.  A common idiom in NumPy is to use the
``np.allclose`` function, which checks whether two values or two arrays equal,
within a small amount of error:

.. nbplot::

    >>> np.pi == 3.1415926
    False
    >>> np.allclose(np.pi, 3.1415926)
    True
    >>> np.allclose([np.pi, 2 * np.pi], [3.1415926, 6.2831852])
    True

*********
np.arange
*********

``arange`` in NumPy is very like the Python ``range`` callable with two
important differences:

* ``arange`` returns an array rather than a ``range`` object (Python 3) or a
  list (Python 2);
* ``arange`` arguments can be floating point values.

.. nbplot::

    >>> np.arange(4, 11, 2)
    array([ 4,  6,  8, 10])
    >>> np.arange(4, 11, 0.5)
    array([  4. ,   4.5,   5. ,   5.5,   6. ,   6.5,   7. ,   7.5,   8. ,
             8.5,   9. ,   9.5,  10. ,  10.5])

Because ``arange`` returns arrays, you can use NumPy element-wise operations
to multiply by the step size and add a start value.  This is one way to create
equally spaced vectors (``np.linspace`` is another):

.. nbplot::

    >>> np.arange(10) * 0.5 + 4
    array([ 4. ,  4.5,  5. ,  5.5,  6. ,  6.5,  7. ,  7.5,  8. ,  8.5])

*******************
Vector dot products
*******************

If I have two vectors :math:`\vec{a}` with elements :math:`a_0, a_1, ...
a_{n-1}`, and :math:`\vec{b}` with elements :math:`b_0, b_1, ... b_{n-1}`
then the `dot product <https://en.wikipedia.org/wiki/Dot_product>`__ is
defined as:

.. math::

   \vec{a} \cdot \vec{b} = \sum_{i=0}^{n-1} a_ib_i = a_0b_0 + a_1b_1 + \cdots + a_{n-1}b_{n-1}

In code:

.. nbplot::

    >>> a = np.arange(5)
    >>> b = np.arange(10, 15)
    >>> np.dot(a, b)
    130
    >>> # The same thing as
    >>> np.sum(a * b)  # Elementwise multiplication
    130

``dot`` is also a *method* of the NumPy array object, and using the method can
be neater and easier to read:

.. nbplot::

    >>> a.dot(b)
    130

*******************
Matrix dot products
*******************

Matrix multiplication operates by taking dot products of the rows of the first
array (matrix) with the columns of the second.

Let's say I have a matrix :math:`\mathbf{X}`, and :math:`\vec{X_{i,:}}` is row
:math:`i` in :math:`\mathbf{X}`. I have a matrix :math:`\mathbf{Y}`, and
:math:`\vec{Y_{:,j}}` is column :math:`j` in :math:`\mathbf{Y}`. The output
matrix :math:`\mathbf{Z} = \mathbf{X} \mathbf{Y}` has entry :math:`Z_{i,j} =
\vec{X_{i,:}} \cdot \vec{Y_{:, j}}`.

.. nbplot::

    >>> X = np.array([[0, 1, 2], [3, 4, 5]])
    >>> X
    array([[0, 1, 2],
           [3, 4, 5]])
    >>> Y = np.array([[7, 8], [9, 10], [11, 12]])
    >>> Y
    array([[ 7,  8],
           [ 9, 10],
           [11, 12]])
    >>> X.dot(Y)
    array([[ 31,  34],
           [112, 124]])

    >>> X[0, :].dot(Y[:, 0])
    31
    >>> X[1, :].dot(Y[:, 0])
    112

*****************
The outer product
*****************

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

We know what will happen if we matrix multiply the row vector and the column
vector:

.. nbplot::

    >>> row_vector.dot(col_vector)
    array([[4]])

What happens with we matrix multiply the column vector by the row vector? We
know this will work because we are multiplying a 3 by 1 array by a 1 by 3
array, so this should generate a 3 by 3 array:

.. nbplot::

    >>> col_vector.dot(row_vector)
    array([[2, 6, 4],
           [0, 0, 0],
           [1, 3, 2]])

This arises from the rules of matrix multiplication, except there is only one
row \* column pair  making up each of the output elements:

.. nbplot::

    >>> print(col_vector[0] * row_vector)
    [[2 6 4]]
    >>> print(col_vector[1] * row_vector)
    [[0 0 0]]
    >>> print(col_vector[2] * row_vector)
    [[1 3 2]]

This (M by 1) vector matrix multiply with a (1 by N) vector is also called the
*outer product* of two vectors. We can generate the same thing from 1D
vectors, by using the numpy ``np.outer`` function:

.. nbplot::

    >>> np.outer(col_vector.ravel(), row_vector.ravel())
    array([[2, 6, 4],
           [0, 0, 0],
           [1, 3, 2]])

*************************
Dot, vectors and matrices
*************************

Unlike MATLAB, Python has one-dimensional vectors. For example, if I slice a
column out of a 2D array of shape (M, N), I do not get a column vector, shape
(M, 1), I get a 1D vector, shape (M,):

.. nbplot::

    >>> X = np.array([[0, 1, 2],
    ...               [3, 4, 5]])
    >>> v = X[:, 0]
    >>> v.shape
    (2,)

Because the 1D vector has lost the idea of being a column rather than a row in
a matrix, it is no longer unambiguous what $v \cdot \mathbf{X}$ means.  It
could be mean a dot product of a row vector shape (1, M) with a matrix shape
(M, N), which is valid |--| or a dot product of a row vector (M, 1) with a
matrix shape (M, N), which is not valid.

If you pass a 1D vector into the ``dot`` function or method, NumPy assumes you
mean it to be a row vector on the left, and a column vector on the right,
which is nearly always what you intended:

.. nbplot::

    >>> # 1D vector is row vector on the left hand side of dot
    >>> v.dot(X)
    array([ 9, 12, 15])

    >>> # 1D vector is column vector on the right hand side of dot
    >>> w = np.array([-1, 0, 1])
    >>> X.dot(w)
    array([2, 2])

Notice that, in both cases, ``dot`` returns a 1D result.

It sometimes helps to make a 1D vector into a 2D row or column vector, to make
your intention explicit, and preserve the 2D shape of the output:

.. nbplot::

    >>> # Turn 1D vector into explicit row vector
    >>> row_v = v.reshape((1, 2))
    >>> # Dot new returns a row vector rather than a 1D vector
    >>> row_v.dot(X)
    array([[ 9, 12, 15]])

***************************************
Adding length 1 dimensions with newaxis
***************************************

NumPy has a nice shortcut for adding a length 1 dimesion to an array.  It is a
little brain-bending, because it operates via array slicing:

.. nbplot::

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

********************
Subtracting the mean
********************

We often want to do operations like subtract the mean from the columns or rows
of a 2D array. For example, here is a 4 by 3 array:

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

One way of doing this, is expanding 1D shape (4,) mean vector out to a shape
(3, 4) array, where the new columns are all the same as the (4,) mean vector.
In fact you can do this with ``np.outer`` and a vector of ones:

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

We'll see later that there are even neater ways to do this, using a technique
called *broadcasting*.

**************
Plotting lines
**************

To plot a line in matplotlib, use ``plot`` with the X coordinates as the first
argument and the matching Y coordinates as the second argument:

.. nbplot::

    >>> # A line from (1, 2) to (7, 11)
    >>> plt.plot([1, 7], [2, 11])
    [...]
    >>> # Another line from (2, 6) to (8, 1)
    >>> plt.plot([2, 8], [6, 1])
    [...]

*****************
Subplots and axes
*****************

We often want to do several plots on the same figure.

We do this with the matplotlib ``subplots`` command.

The standard input arguments to ``subplots`` are the number of rows and the
number of columns you want in your grid of axes. For example, if you want two
plots underneath each other you would call ``subplots(2, 1)`` for two rows and
one column.

``subplots`` returns a ``figure`` object, that is an object representing the
figure containing the axes. It also returns a list of ``axes``. The axes are
objects representing the axes on which we can plot. The axis objects have
methods like ``plot`` and ``imshow`` that allow us to plot on the given axes:

.. nbplot::

    >>> x = np.arange(0, np.pi * 2, 0.1)
    >>> fig, axes = plt.subplots(2, 1)
    >>> axes[0].plot(x, np.sin(x))
    [...]
    >>> axes[1].plot(x, np.cos(x))
    [...]

.. Also:

    plotting lines

