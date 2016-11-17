####################################################################
Applying coordinate transforms with ``nibabel.affines.apply_affine``
####################################################################

We often want to apply an affine to an array of coordinates, where the last
axis of the array is length 3, containing the x, y and z coordinates.

Nibabel uses ``nibabel.affines.apply_affine`` for this.

For background see: :doc:`nibabel_affines`.

.. nbplot::

    >>> import numpy as np
    >>> from nibabel.affines import from_matvec, to_matvec, apply_affine

.. nbplot::

    >>> points = np.array([[0, 1, 2], [2, 2, 4], [3, -2, 1], [5, 3, 1]])
    >>> points
    array([[ 0,  1,  2],
           [ 2,  2,  4],
           [ 3, -2,  1],
           [ 5,  3,  1]])

.. nbplot::

    >>> zooms_plus_translations = from_matvec(np.diag([3, 4, 5]),
    ...                                       [11, 12, 13])
    >>> zooms_plus_translations
    array([[ 3,  0,  0, 11],
           [ 0,  4,  0, 12],
           [ 0,  0,  5, 13],
           [ 0,  0,  0,  1]])

.. nbplot::

    >>> apply_affine(zooms_plus_translations, points)
    array([[11, 16, 23],
           [17, 20, 33],
           [20,  4, 18],
           [26, 24, 18]])

Of course, this is the same as:

.. nbplot::

    >>> mat, vec = to_matvec(zooms_plus_translations)
    >>> mat.dot(points.T).T + vec.reshape((1, 3))
    array([[11, 16, 23],
           [17, 20, 33],
           [20,  4, 18],
           [26, 24, 18]])

The advantage of ``nib.affines.apply_affine`` is that it can deal with arrays
of more than two dimensions, and it transposes the transformation matrices for
you to apply the transforms correctly.

A typical use is when applying extra affine transformations to a X by Y by Z
by 3 array of coordinates.
