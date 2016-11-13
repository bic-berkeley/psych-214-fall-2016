#############################
Resampling with scipy.ndimage
#############################

.. nbplot::
    :include-source: false

    >>> # compatibility with Python 2
    >>> from __future__ import print_function
    >>> from __future__ import division

.. nbplot::

    >>> # import common modules
    >>> import numpy as np
    >>> np.set_printoptions(precision=4)  # print arrays to 4DP
    >>> import matplotlib.pyplot as plt

*********************
Reampling, pull, push
*********************

Let us say we have two images :math:`\mathbf{I}` and :math:`\mathbf{J}`.

There is some spatial transform between them, such as a translation, or
rotation.

We could either think of the transformation that maps :math:`\mathbf{I} \to
\mathbf{J}` or :math:`\mathbf{J} \to \mathbf{I}`.

The transformations map voxel coordinates in one image to coordinates in the
other.

For example, write a coordinate in :math:`\mathbf{I}` as :math:`(x_i, y_i,
z_i)`, and a coordinate in :math:`\mathbf{J}` as :math:`(x_j, y_j, z_j)`.

The mapping :math:`\mathbf{I} \to \mathbf{J}` maps :math:`(x_i, y_i, z_i) \to
(x_j, y_j, z_j)`.

Now let us say that we want to move image :math:`\mathbf{J}` to match image
:math:`\mathbf{I}`.

To do this moving, we need to resample :math:`\mathbf{J}` onto the same voxel
grid as :math:`\mathbf{I}`.

Specifically, we are going to do the following:

* make a new empty image :math:`\mathbf{K}` that has the same voxel
  grid as :math:`\mathbf{I}`;
* for each coordinate in :math:`\mathbf{I} : (x_i, y_i, z_i)` we will apply
  the transform :math:`\mathbf{I} \to \mathbf{J}` to get :math:`(x_j, y_j,
  z_j)`;
* we will probably need to estimate a value :math:`v` from :math:`\mathbf{J}`
  at :math:`(x_j, y_j, z_j)` because the coordinate values :math:`(x_j, y_j,
  z_j)` will probably not be integers, and so there is no exactly matching
  value in :math:`\mathbf{J}`;
* we place :math:`v` into :math:`\mathbf{K}` at coordinate :math:`(x_i, y_i,
  z_i)`.

Notice that, in order to move :math:`\mathbf{J}` to match :math:`\mathbf{I}`
we needed the opposite transform |--| that is: :math:`\mathbf{I} \to
\mathbf{J}`.  This is called *pull resampling*.

We will call the :math:`\mathbf{I} \to \mathbf{J}` transform the *resampling
transform*.

**********************************
Scipy ndimage and affine_transform
**********************************

Scipy has a function for doing reampling with transformations, called
`scipy.ndimage.affine_transform`_.

.. nbplot::

    >>> from scipy.ndimage import affine_transform

It does all the heavy work of resampling for us.

For example, lets say we have an image volume :math:`\mathbf{I}`
(:download:`ds107_sub012_t1r2.nii`):

.. nbplot::

    >>> import nibabel as nib
    >>> img = nib.load('ds107_sub012_t1r2.nii')
    >>> data = img.get_data()
    >>> I = data[..., 0]  # I is the first volume

We have another image volume :math:`\mathbf{J}`:

.. nbplot::

    >>> J = data[..., 1]  # I is the second volume

Let's say we know that the resampling transformation :math:`\mathbf{I} \to
\mathbf{J}` is given by:

* a rotation by 0.2 radians about the x axis;
* a translation of [1, 2, 3] voxels.

See :doc:`rotations_2d_3d` for more on 2D and 3D rotation matrices.

Download the file :download:`rotations.py`. It has routines that will make
3 by 3 rotation matrices for rotations by given angles around the x, y, and z
axes.

Of course you will want to test these functions. Download
:download:`test_rotations.py` to the same directory as ``rotations.py`` and
run the following from your terminal::

    py.test test_rotations.py

We use the routines in ``rotation.py`` to make the rotation matrix we need:

.. nbplot::

    >>> from rotations import x_rotmat  # from rotations.py
    >>> # rotation matrix for rotation of 0.2 radians around x axis
    >>> M = x_rotmat(0.2)
    >>> M
    array([[ 1.    ,  0.    ,  0.    ],
           [ 0.    ,  0.9801, -0.1987],
           [ 0.    ,  0.1987,  0.9801]])
    >>> translation = [1, 2, 3]  # Translation from I to J
    >>> translation
    [1, 2, 3]

The ``affine_transform`` function does the work of resampling:

.. nbplot::

    >>> # order=1 for linear interpolation
    >>> K = affine_transform(J, M, translation, order=1)
    >>> K.shape
    (64, 64, 35)

``affine_transform`` implements the following algorithm:

* makes the new empty volume ``K``, assuming it will be the same shape as
  ``J``;
* for each coordinate :math:`(x_i, y_i, z_i)` implied by the volume ``K``:

   * apply the transformations implied by ``M`` and ``translation`` to
     :math:`(x_i, y_i, z_i)` to get the corresponding point in ``J`` :
     :math:`(x_j, y_j, z_j)`;
   * resample ``J`` at :math:`(x_j, y_j, z_j)` to get :math:`v`;
   * place :math:`v` at :math:`(x_i, y_i, z_i)` in ``K``
