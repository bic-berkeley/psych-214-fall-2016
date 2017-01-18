##########################################
Vector and matrix dot products, "np.outer"
##########################################

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
    >>> row_vector.shape
    (1, 3)
    >>> row_vector
    array([[1, 3, 2]])

A column vector is a 2D vector where the second dimension is length 1.

.. nbplot::

    >>> col_vector = np.array([[2], [0], [1]])
    >>> col_vector.shape
    (3, 1)
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

.. _dot-vectors-matrices:

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
