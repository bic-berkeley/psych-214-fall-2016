.. vim: ft=rst

########################
Extra transform exercise
########################

.. nbplot::
    :include-source: false

    >>> # compatibility with Python 2
    >>> from __future__ import print_function
    >>> from __future__ import division

.. nbplot::

    >>> #: standard imports
    >>> import numpy as np
    >>> import numpy.linalg as npl
    >>> import matplotlib.pyplot as plt
    >>> # print arrays to 4 decimal places
    >>> np.set_printoptions(precision=4, suppress=True)
    >>> import nibabel as nib

.. nbplot::

    >>> #: gray colormap and nearest neighbor interpolation by default
    >>> plt.rcParams['image.cmap'] = 'gray'
    >>> plt.rcParams['image.interpolation'] = 'nearest'

**************************
What transforms did I add?
**************************

I took this image

* :download:`ds114_sub009_highres.nii`

and I made a new copy, in ``img, hdr`` format (see
:doc:`image_header_and_affine`):

* :download:`ds114_sub009_highres_moved.img`;
  :download:`ds114_sub009_highres_moved.hdr`.

I then modified the affine in ``ds114_sub009_highres_moved.hdr`` to add an
extra rotation and translation.

.. The script to do the transform is make_ds114_anat.py

What extra translation and rotation did I add?

Hint: remember the rotation formulae from :doc:`rotation_2d_3d`:

.. math::

   \begin{alignat}{1}
   R_x(\theta) &= \begin{bmatrix}
   1 & 0 & 0 \\
   0 & \cos \theta &  -\sin \theta \\[3pt]
   0 & \sin \theta  &  \cos \theta \\[3pt]
   \end{bmatrix} \\[6pt]
   R_y(\theta) &= \begin{bmatrix}
   \cos \theta & 0 & \sin \theta \\[3pt]
   0 & 1 & 0 \\[3pt]
   -\sin \theta & 0 & \cos \theta \\
   \end{bmatrix} \\[6pt]
   R_z(\theta) &= \begin{bmatrix}
   \cos \theta &  -\sin \theta & 0 \\[3pt]
   \sin \theta & \cos \theta & 0\\[3pt]
   0 & 0 & 1\\
   \end{bmatrix}
   \end{alignat}

You might also want to compare against results from the
:download:`rotations.py` module:

.. nbplot::

    >>> #: functions to make rotation matrices
    >>> from rotations import x_rotmat, y_rotmat, z_rotmat

Final hint:

* inverse sine, cosine are ``np.arcsin, np.arccos``.

.. nbplot::

    >>> #: Get the original image affine
    >>> import nibabel as nib
    >>> orig_img = nib.load('ds114_sub009_highres.nii')
    >>> print(orig_img.affine)
    [[   0.9989   -0.0605    0.0109 -129.8257]
     [   0.0427    1.263     0.2336 -119.0906]
     [  -0.0215   -0.3028    0.9723 -143.4178]
     [   0.        0.        0.        1.    ]]

.. nbplot::

    >>> #: Get the new image affine
    >>> moved_img = nib.load('ds114_sub009_highres_moved.img')
    >>> moved_img.affine
    array([[   0.9416,   -0.4311,   -0.0586,  -98.8336],
           [   0.336 ,    1.1887,    0.2264, -164.1377],
           [  -0.0215,   -0.3028,    0.9723, -158.4178],
           [   0.    ,    0.    ,    0.    ,    1.    ]])

.. nbplot::

    >>> #- Work out what transform has been added in the new affine
    >>> extra = moved_img.affine.dot(npl.inv(orig_img.affine))
    >>> extra
    array([[  0.9553,  -0.2955,   0.    , -10.    ],
           [  0.2955,   0.9553,   0.    , -12.    ],
           [  0.    ,  -0.    ,   1.    , -15.    ],
           [  0.    ,   0.    ,   0.    ,   1.    ]])

.. nbplot::

    >>> #- What rotation and translation has been applied?
    >>> z_angle = np.arccos(extra[0, 0])
    >>> translation = extra[:3, 3]
    >>> z_angle, translation
    (0.3000000..., array([-10., -12., -15.]))
