###################
Reshaping, 4D to 2D
###################

See also: :doc:`voxels_by_time`.

**************
Revision on 3D
**************

We often find ourselves doing complicated reshape operations when we are
dealing with images.   For example, we may find ourselves reshaping the first
few dimensions, but leaving the last intact:

.. nbplot::

    >>> import numpy as np
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

See also: :doc:`reshape_and_3d`.

*****
To 4D
*****

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
