########################
Four dimensions exercise
########################

* For code template see: :download:`four_dimensions_code.py`;
* For solution see: :doc:`four_dimensions_solution`.


.. nbplot::
    :include-source: false


.. nbplot::

    >>> #: Our usual imports
    >>> import numpy as np  # the Python array package
    >>> import matplotlib.pyplot as plt  # the Python plotting package

We are going to load a four-dimensional (X, Y, Z, t) BOLD image called
:download:`ds107_sub012_t1r2.nii`. Download the file using the link.  Import
the ``nibabel`` module, and load the image with nibabel to create an image
object.

.. nbplot::

    >>> #- Load image object using nibabel
    >>> #- Turn off nibabel memory mapping.

In the usual way get the array data from this image and show the image shape.

.. nbplot::

    >>> #- Get image array data from image object

Select the 10th volume (time index 9) from 4D image data array, by slicing
over the last dimension. What shape is it?

.. nbplot::

    >>> #- Get the 10th volume and show shape

Get the standard deviation across all voxels in this 3D volume:

.. nbplot::

    >>> #- Standard deviation across all voxels for 10th volume

Loop over all volumes in the 4D image and store the standard deviation for
each volume in a list. Plot these to see if there are any volumes with
particularly unusual standard deviation.

.. nbplot::

    >>> #- Get standard deviation for each volume; then plot the values

SPM uses a measure called "global signal" to give a very rough estimate of the
average signal value within the brain. The idea is that you need a threshold
to select voxels with signal high enough to be inside the brain, and not in
the air around the brain, which has very low (near 0) signal.

The algorithm goes like this.

*  Get a single 3D volume V;
*  Calculate the mean signal of the voxels in V; call that M;
*  Make a threshold T where T = M / 8.
*  Select all voxel values in V that are greater than T; call these values W;
*  Return the mean of all values in W.

See `SPM global image signal
<http://imaging.mrc-cbu.cam.ac.uk/imaging/PrinciplesStatistics#Global_image_signal>`__.

In the SPM code, the algorithm is implemented in a MATLAB function called
``spm_global``.

I used the MATLAB script :download:`get_global_signals.m` to run the
``spm_global`` MATLAB function on the volumes of ``ds107_sub012_t1r2.nii``.
The script saved the SPM global values to a text file
:download:`global_signals.txt`. The first four lines of the
``global_signals.txt`` file look like this:

::

    376.53
    375.75
    375.26
    376.01

Read these global values calculated by SPM into a list, and plot the values.

.. nbplot::

    >>> #- Read global signal values calculated by SPM, and plot

Now implement the algorithm above to recalculate the SPM global signal for the
first volume (volume index zero). Hint: you will likely need to index using a
boolean (mask) array. Remember, the steps are:

*  Get a single 3D volume V;
*  Calculate the mean signal of the voxels in V; call that M;
*  Make a threshold T where T = M / 8.
*  Select all voxel values in V that are greater than T; call these values W;
*  Get the mean of all values in W.

You should get the same value as SPM - the first value you read from
``global_signals.txt``.

.. nbplot::

    >>> #- Apply algorithm for SPM global calculation to first volume

Make a function called ``spm_global`` that accepts a 3D array as input, and
returns the global signal using the SPM algorithm. Call that function on the
first volume to show that it is working (as in ``print(spm_global(data[:, :,
:, 0]))``).

.. nbplot::

    >>> #- Make an `spm_global` function that accepts a 3D array as input,
    >>> #- and returns the global mean for the volume according to the SPM
    >>> #- algorithm

Make a function called ``get_spm_globals`` that accepts an image filename as
an argument. The function will load the image, get the array data for the
image, use your new ``spm_global`` function calculate the global value for
each volume, and return these values as a list.  Finally, show this is working
by plotting the values for the ``ds107_sub012_t1r2.nii`` image with something
like:

::

    all_globals = get_spm_globals('ds107_sub012_t1r2.nii')
    plt.plot(all_globals)

.. nbplot::

    >>> #- Write a function `get_spm_globals` that returns the global values 
    >>> #- for each volume
