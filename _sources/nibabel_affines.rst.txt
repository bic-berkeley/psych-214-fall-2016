#############################
The `nibabel.affines`_ module
#############################

.. nbplot::

    >>> import numpy as np
    >>> np.set_printoptions(precision=4, suppress=True)
    >>> import nibabel as nib

Neuroimaging images have affines, and we often need to process these
affines, or apply these affines to coordinates.

Nibabel has routines to do this in its ``affines`` submodule.

The ``from_matvec`` function is a short-cut to make a 4 x 4 affine matrix from
a 3 x 3 matrix and an (optional) vector of translations.

For example, let's say I have a 3 x 3 rotation matrix, specifying a rotation
of 0.4 radians around the y axis (see :doc:`rotation_2d_3d`):

.. nbplot::

    >>> cos_a = np.cos(0.4)
    >>> sin_a = np.sin(0.4)
    >>> y_rotation = np.array([[ cos_a,    0,  sin_a],
    ...                        [     0,    1,      0],
    ...                        [-sin_a,    0,  cos_a]])
    >>> y_rotation
    array([[ 0.9211,  0.    ,  0.3894],
           [ 0.    ,  1.    ,  0.    ],
           [-0.3894,  0.    ,  0.9211]])

I want to put this 3 x 3 matrix into a 4 x 4 affine matrix:

.. nbplot::

    >>> # Affine from a 3x3 matrix (the 'mat' in 'matvec')
    >>> nib.affines.from_matvec(y_rotation)
    array([[ 0.9211,  0.    ,  0.3894,  0.    ],
           [ 0.    ,  1.    ,  0.    ,  0.    ],
           [-0.3894,  0.    ,  0.9211,  0.    ],
           [ 0.    ,  0.    ,  0.    ,  1.    ]])

You can also add a translation vector in the call to ``from_matvec``.  The
translation vector is the ``vec`` of ``from_matvec``:

.. nbplot::

    >>> # Affine from a 3x3 matrix ('mat') and a translation vector ('vec')
    >>> aff = nib.affines.from_matvec(y_rotation, [10, 20, 30])
    >>> aff
    array([[  0.9211,   0.    ,   0.3894,  10.    ],
           [  0.    ,   1.    ,   0.    ,  20.    ],
           [ -0.3894,   0.    ,   0.9211,  30.    ],
           [  0.    ,   0.    ,   0.    ,   1.    ]])

``nibabel.affines.to_matvec`` does the reverse operation.  It splits the
affine matrix into the top left 3 x 3 matrix, and the translation vector from
the last column of the affine:

.. nbplot::

    >>> mat, vec = nib.affines.to_matvec(aff)
    >>> mat
    array([[ 0.9211,  0.    ,  0.3894],
           [ 0.    ,  1.    ,  0.    ],
           [-0.3894,  0.    ,  0.9211]])
    >>> vec
    array([ 10.,  20.,  30.])
