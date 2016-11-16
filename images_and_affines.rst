##################
Images and affines
##################

See: `coordinate systems and affine transforms`_ for background.

.. nbplot::
    :include-source: false

    >>> # compatibility with Python 2
    >>> from __future__ import print_function
    >>> from __future__ import division

.. nbplot::

    >>> # import common modules
    >>> import numpy as np
    >>> # print arrays to 4DP
    >>> np.set_printoptions(precision=4, suppress=True)
    >>> import numpy.linalg as npl
    >>> import nibabel as nib

*****************
Affines, inverses
*****************

We often have the situation where we compose an affine of several
transformations. We do the composing using matrix multiplication. For example,
the following code composes two rotations and a translation.  We are using the
:download:`rotations.py` module to make the :doc:`3D rotation matrices
<rotation_2d_3d>`.  Remember |--| matrix multiplication works right to left.

.. nbplot::

    >>> # get functions to make 3D rotation matrices
    >>> from rotations import x_rotmat, y_rotmat, z_rotmat

Here is a rotation matrix (3 x 3) for a rotation of -0.2 radians around the x
axis:

.. nbplot::

    >>> first_rotation = x_rotmat(-0.2)
    >>> first_rotation
    array([[ 1.    ,  0.    ,  0.    ],
           [ 0.    ,  0.9801,  0.1987],
           [ 0.    , -0.1987,  0.9801]])

We can make this rotation matrix into an affine transformation, by putting it
into the top left of a 4 x 4 identity matrix:

.. nbplot::

    >>> first_affine = np.eye(4)  # The identity affine
    >>> first_affine[:3, :3] = first_rotation
    >>> first_affine
    array([[ 1.    ,  0.    ,  0.    ,  0.    ],
           [ 0.    ,  0.9801,  0.1987,  0.    ],
           [ 0.    , -0.1987,  0.9801,  0.    ],
           [ 0.    ,  0.    ,  0.    ,  1.    ]])

Now we made a second affine matrix for a rotation around y of 0.4 radians:

.. nbplot::

    >>> second_affine = np.eye(4)
    >>> second_affine[:3, :3] = y_rotmat(0.4)
    >>> second_affine
    array([[ 0.9211,  0.    ,  0.3894,  0.    ],
           [ 0.    ,  1.    ,  0.    ,  0.    ],
           [-0.3894,  0.    ,  0.9211,  0.    ],
           [ 0.    ,  0.    ,  0.    ,  1.    ]])

Finally we make a translation of 10 in x, 20 in y and 30 in z:

.. nbplot::

    >>> third_affine = np.eye(4)
    >>> third_affine[:3, 3] = [10, 20, 30]
    >>> third_affine
    array([[  1.,   0.,   0.,  10.],
           [  0.,   1.,   0.,  20.],
           [  0.,   0.,   1.,  30.],
           [  0.,   0.,   0.,   1.]])

We compose these three affine matrices to give an affine implementing *first*
a rotation of -0.2 around the x axis, *then* a rotation of 0.4 around the y
axis, and *finally* a translation [10, 20, 30] in [x, y, z]. Note the order
|--| matrix multiplication goes from right to left:

.. nbplot::

    >>> combined = third_affine.dot(second_affine.dot(first_affine))
    >>> combined
    array([[  0.9211,  -0.0774,   0.3817,  10.    ],
           [  0.    ,   0.9801,   0.1987,  20.    ],
           [ -0.3894,  -0.183 ,   0.9027,  30.    ],
           [  0.    ,   0.    ,   0.    ,   1.    ]])

*****************************
The `nibabel.affines`_ module
*****************************

In fact, nibabel has a short-cut routine to make a 4x4 affine matrix from a
3 x 3 matrix and an (optional) vector of translations:

.. nbplot::

    >>> # Affine from a 3x3 matrix (the 'mat' in 'matvec')
    >>> nib.affines.from_matvec(y_rotmat(0.4))
    array([[ 0.9211,  0.    ,  0.3894,  0.    ],
           [ 0.    ,  1.    ,  0.    ,  0.    ],
           [-0.3894,  0.    ,  0.9211,  0.    ],
           [ 0.    ,  0.    ,  0.    ,  1.    ]])

.. nbplot::

    >>> # Affine from a 3x3 matrix ('mat') and a translation vector ('vec')
    >>> nib.affines.from_matvec(y_rotmat(0.4), [10, 20, 30])
    array([[  0.9211,   0.    ,   0.3894,  10.    ],
           [  0.    ,   1.    ,   0.    ,  20.    ],
           [ -0.3894,   0.    ,   0.9211,  30.    ],
           [  0.    ,   0.    ,   0.    ,   1.    ]])

**********************************
Manipulating affines with inverses
**********************************

Let us say we have an affine, like the one we just made:

.. nbplot::

    >>> combined
    array([[  0.9211,  -0.0774,   0.3817,  10.    ],
           [  0.    ,   0.9801,   0.1987,  20.    ],
           [ -0.3894,  -0.183 ,   0.9027,  30.    ],
           [  0.    ,   0.    ,   0.    ,   1.    ]])

Imagine that we knew that this affine was composed of three affines, and we
knew the last two, but not the first. How would we find what the first affine
was?

Call our combined affine :math:`\mathbf{D}`. We know that :math:`\mathbf{D} =
\mathbf{C} \cdot \mathbf{B} \cdot \mathbf{A}`. We know :math:`\mathbf{C}` and
:math:`\mathbf{B}` but we want to find :math:`\mathbf{A}`.

Above I've written matrix multiplication with a dot - as in :math:`\mathbf{B}
\cdot \mathbf{A}`, but in what follows I'll omit the dot, just writing
:math:`\mathbf{B} \mathbf{A}` to mean matrix multiplication.

We find :math:`\mathbf{A}` using matrix inverses. Call :math:`\mathbf{E} =
\mathbf{C} \mathbf{B}`. Then :math:`\mathbf{D} = \mathbf{E} \mathbf{A}`. If we
can find the inverse of :math:`\mathbf{E}` (written as
:math:`\mathbf{E^{-1}}`) then (by the definition of the inverse):

.. math::

   \mathbf{E^{-1}} \mathbf{E} = \mathbf{I}

and:

.. math::

   \mathbf{E^{-1}} \mathbf{D} = \mathbf{E^{-1}} \mathbf{E} \mathbf{A} \\
   \mathbf{E^{-1}} \mathbf{D} = \mathbf{I} \mathbf{A} \\
   \mathbf{E^{-1}} \mathbf{D} = \mathbf{A}

For reasons we do not have time to go into, our affine matrices are almost
invariably invertible.

Let's see if we can reconstruct our ``first_affine`` from the ``combined``
affine, given we know the ``third_affine`` and ``second_affine``:

.. nbplot::

    >>> E = third_affine.dot(second_affine)
    >>> E_inv = npl.inv(E)
    >>> E_inv.dot(combined)  # doctest: +SKIP
    array([[ 1.    ,  0.    , -0.    ,  0.    ],
           [ 0.    ,  0.9801,  0.1987,  0.    ],
           [ 0.    , -0.1987,  0.9801,  0.    ],
           [ 0.    ,  0.    ,  0.    ,  1.    ]])

This is the same as our first affine:

.. nbplot::

    >>> first_affine
    array([[ 1.    ,  0.    ,  0.    ,  0.    ],
           [ 0.    ,  0.9801,  0.1987,  0.    ],
           [ 0.    , -0.1987,  0.9801,  0.    ],
           [ 0.    ,  0.    ,  0.    ,  1.    ]])
    >>> np.allclose(E_inv.dot(combined), first_affine)
    True

What about the situation where we know the first part of the affine, but we
want to find the rest?

To solve this problem, we will need the *right inverse*.

The inverse we have used so far is the *left inverse* - so called because we
apply it multiplying on the left of the original matrix:

.. math::

   \mathbf{E^{-1}} \mathbf{E} = \mathbf{I}

Luckily, it turns out that, for square matrices, if there is a *left inverse*
:math:`\mathbf{E^{-1}}` then this is also the right inverse:

.. math::

   \mathbf{E^{-1}} \mathbf{E} = \mathbf{E} \mathbf{E^{-1}} = \mathbf{I}

It is a bit out of our way to prove that a matrix with a left inverse must
also have a right inverse.  If you accept that on faith for now, it is easy to
prove that, if there is a right inverse, it must be the same as the left
inverse. Call the left inverse :math:`\mathbf{L}` and the right inverse
:math:`\mathbf{R}`:

.. math::

   \mathbf{LA} = \mathbf{I}\\
   \mathbf{AR} = \mathbf{I}\\

then:

.. math::

   \mathbf{LAR} = \mathbf{LAR}\\
   \mathbf{L(AR)} = \mathbf{(LA)R}\\
   \mathbf{L} = \mathbf{R}

So, in our case, where we want to find the transformations *following* the
first affine, we can do this:

.. math::

   \mathbf{F} \triangleq \mathbf{C} \mathbf{B} \\
   \mathbf{D} = \mathbf{F} \mathbf{A} \\
   \mathbf{D} \mathbf{A^{-1}} = \mathbf{F} \mathbf{A} \mathbf{A^{-1}} \\
   \mathbf{D} \mathbf{A^{-1}} = \mathbf{F}

For our actual affines:

.. nbplot::

    >>> third_with_second = combined.dot(npl.inv(first_affine))
    >>> third_with_second  # doctest: +SKIP
    array([[  0.9211,  -0.    ,   0.3894,  10.    ],
           [  0.    ,   1.    ,   0.    ,  20.    ],
           [ -0.3894,  -0.    ,   0.9211,  30.    ],
           [  0.    ,   0.    ,   0.    ,   1.    ]])

.. nbplot::

    >>> # This is the same as
    >>> F = third_affine.dot(second_affine)
    >>> F  # doctest: +SKIP
    array([[  0.9211,   0.    ,   0.3894,  10.    ],
           [  0.    ,   1.    ,   0.    ,  20.    ],
           [ -0.3894,   0.    ,   0.9211,  30.    ],
           [  0.    ,   0.    ,   0.    ,   1.    ]])
    >>> np.allclose(third_with_second, F)
    True
