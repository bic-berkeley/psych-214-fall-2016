################################
Reshaping 4D images to 2D arrays
################################

See also: :doc:`reshape_and_4d`.

.. nbplot::
    :include-source: false

    >>> # compatibility with Python 2
    >>> from __future__ import print_function, division

.. nbplot::

    >>> #: import common modules
    >>> import numpy as np  # the Python array package
    >>> import matplotlib.pyplot as plt  # the Python plotting package
    >>> # Display array values to 6 digits of precision
    >>> np.set_printoptions(precision=4, suppress=True)

In this example, we calculate the standard deviation across voxels at each
time point.

We're working on :download:`ds114_sub009_t2r1.nii`.  This is a 4D FMRI image.

.. nbplot::

    >>> import nibabel as nib
    >>> img = nib.load('ds114_sub009_t2r1.nii')
    >>> img.shape
    (64, 64, 30, 173)

We want to calculate the standard deviation across all voxels.  Remember that
a :term:`voxel` is a pixel with volume, and refers to a position in space.
Therefore we have this number of voxels in each volume:

.. nbplot::

    >>> n_voxels = np.prod(img.shape[:-1])
    >>> n_voxels
    122880

To calculate the standard deviation across voxels, we could loop across all
volumes, and calculate the standard deviation for each volume:

.. nbplot::

    >>> n_trs = img.shape[-1]
    >>> data = img.get_data()
    >>> std_devs = []
    >>> for vol_no in range(n_trs):
    ...     vol = data[..., vol_no]
    ...     std_devs.append(np.std(vol))
    ...
    >>> plt.plot(std_devs)
    [...]

We could also flatten the three voxel axes out into one long voxel axis, using
reshape |--| see: :doc:`reshape_and_4d`.  Then we can use the ``axis``
parameter to the ``np.std`` function to calculate the standard deviation
across voxels, in one shot.  This is "vectorizing", where we take an operation
that needed a loop, and use array operations to do the work instead:

.. nbplot::

    >>> voxels_by_time = data.reshape((n_voxels, n_trs))
    >>> std_devs_vectorized = np.std(voxels_by_time, axis=0)
    >>> assert np.allclose(std_devs_vectorized, std_devs)
