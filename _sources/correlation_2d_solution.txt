############################
Correlation per voxel, in 2D
############################

In this exercise, we will take each voxel time course in the brain, and
calculate a correlation between the task-on / task-off vector and the voxel
time course.  We then make a new 3D volume that contains correlation values
for each voxel.

You've done this before in the exercise :doc:`voxel_correlation_exercise`, but
this time we'll do it by reshaping the 4D data to 2D, and looping over the
long voxels axis instead of over each of the three spatial axes.

We've given you the stuff you will have done already for the previous exercise
|--| you can copy-paste into IPython.

.. nbplot::
    :include-source: false

    >>> # Python 2 compatibility
    >>> from __future__ import print_function, division

.. nbplot::

    >>> #: Standard imports
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> import nibabel as nib

.. nbplot::

    >>> #: import events2neural from stimuli module
    >>> from stimuli import events2neural

    >>> #: Load the ds114_sub009_t2r1.nii image
    >>> img = nib.load('ds114_sub009_t2r1.nii')

    >>> #: Get the number of volumes in ds114_sub009_t2r1.nii
    >>> n_trs = img.shape[-1]

The TR (time between scans) is 2.5 seconds.

.. nbplot::

    >>> TR = 2.5

Call the ``events2neural`` function to give you a time course that is 1
for the volumes during the task (thinking of verbs) and 0 for the
volumes during rest.

.. nbplot::

    >>> #: Call events2neural to give on-off values for each volume
    >>> time_course = events2neural('ds114_sub009_t2r1_cond.txt', 2.5, n_trs)

.. nbplot::

    >>> #: Drop the first 4 volumes, and the first 4 on-off values
    >>> data = img.get_data()
    >>> data = data[..., 4:]
    >>> time_course = time_course[4:]

.. nbplot::

    >>> #- Calculate the number of voxels (number of elements in one volume)
    >>> n_voxels = np.prod(data.shape[:-1])

Reshape the 4D data to a 2D array shape (number of voxels, number
of volumes).

.. nbplot::

    >>> #- Reshape 4D array to 2D array n_voxels by n_volumes
    >>> data_2d = np.reshape(data, (n_voxels, data.shape[-1]))

.. nbplot::

    >>> #- Make a 1D array of size (n_voxels,) to hold the correlation values
    >>> correlations_1d = np.zeros((n_voxels,))

Loop over all voxels, calculate the correlation coefficient with
``time_course`` at this voxel, and fill in the corresponding entry in your 1D
array.

.. nbplot::

    >>> #- Loop over voxels filling in correlation at this voxel
    >>> for i in range(n_voxels):
    ...     correlations_1d[i] = np.corrcoef(time_course, data_2d[i, :])[0, 1]

Reshape the correlations 1D array back to a 3D array, using the original 3D
shape.

.. nbplot::

    >>> #- Reshape the correlations array back to 3D
    >>> correlations = np.reshape(correlations_1d, data.shape[:-1])

If all went well, you should have generated the same 3D volume of correlations
as you did for the original exercise:

.. nbplot::

    >>> #- Plot the middle slice of the third axis from the correlations array
    >>> plt.imshow(correlations[:, :, 14], cmap='gray')
    <...>
