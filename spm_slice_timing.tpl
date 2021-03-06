.. vim: ft=rst

#########################
SPM slice timing solution
#########################

Requirements:

* :doc:`introducing_nipype`;
* :doc:`saving_images`;
* `slice timing`_;
* :doc:`tr_and_headers`;

.. nbplot::
    :include-source: false

    >>> # compatibility with Python 2
    >>> from __future__ import print_function
    >>> from __future__ import division

.. nbplot::

    >>> #: standard imports
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> # print arrays to 4 decimal places
    >>> np.set_printoptions(precision=4, suppress=True)
    >>> import numpy.linalg as npl
    >>> import nibabel as nib

.. nbplot::

    >>> #: gray colormap and nearest neighbor interpolation by default
    >>> plt.rcParams['image.cmap'] = 'gray'
    >>> plt.rcParams['image.interpolation'] = 'nearest'

******************
Preparing the data
******************

We will be using the functional image :download:`ds114_sub009_t2r1.nii`.

In :doc:`four_dimensions_exercise` we found that the first volumes had higher
signal than the rest of the volumes in the time-series.  To start, we drop the
first four volumes, and save the new 4D image to disk (:doc:`saving_images`):

.. nbplot::

    >>> #: save new copy of image with first four volumes dropped
    >>> img = nib.load('ds114_sub009_t2r1.nii')
    >>> data = img.get_data()
    >>> fixed = nib.Nifti1Image(data[..., 4:], img.affine, img.header)
    >>> nib.save(fixed, 'fds114_sub009_t2r1.nii')

*******************************
Parameters for SPM slice timing
*******************************

To prepare for `slice timing`_ with SPM, we need first need some parameters,
to give SPM the information it needs on when the slices were collected.

First we need the number of "slices" (length of the third image dimension):

.. nbplot::

    >>> #: load the fixed "f" image to get parameters
    >>> img = nib.load('fds114_sub009_t2r1.nii')
    >>> num_slices = img.shape[2]
    >>> num_slices
    30

Next we need the TR.  We can't always get the correct TR from the image header
(see :doc:`tr_and_headers`), but we can in this case.

.. nbplot::

    >>> #: get the TR from this image
    >>> TR = img.header.get_zooms()[-1]
    >>> TR
    2.5

We need the time to acquire *all but the last slice*. SPM calls this ``TA``
(time of acquisition).  This odd parameter comes from deep in the history of
the SPM slice-timing routine.

.. nbplot::

    >>> #: calculate TA
    >>> time_for_one_slice = TR / num_slices
    >>> TA = TR - time_for_one_slice
    >>> TA
    2.41666...

Next we need the acquisition order. This is a list ``acq_order`` of length
``num_slices`` where ``acq_order[i]`` gives the slice index of the slice
acquired at position ``i`` in time.

SPM uses MATLAB.  We are going to pass these parameters to SPM.  Because this
is for MATLAB, the array indices start at 1 rather than 0 as they do for
Python.

So, if ``acq_order`` is ``[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]`` that means
that the first slice acquired was (1-based) slice index 1, followed by
slice index 3, followed by slice index 5, and so on.

For our image, the scanner collected the odd index slices first, starting at
the bottom, and then came back and collected the even index slices:

.. nbplot::

    >>> # - generate acq_order list
    >>> odd = range(1, num_slices+1, 2)
    >>> even = range(2, num_slices+1, 2)
    >>> acq_order = list(odd) + list(even)
    >>> acq_order
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

Lastly, SPM slice timing also asks for a *reference slice*. This is the
(1-based) index of the slice to which the others will be matched in terms of
time. For example, if we want to use the interpolation to match the times of
all the slices to the acquisition time of the first slice, the reference slice
would be 1 (bottom slice, with 1-based indexing).

Now we can use the SPM interface to run the slice timing in the SPM GUI:

***********************************
Batching using the nipype interface
***********************************

We are going to use the nipype_ interface to run the same thing.

If you just ran SPM slice timing via the GUI, delete the image that SPM saved:

.. nbplot::

    >>> #: import the routines for working with the operating system
    >>> import os
    >>> # Delete file if it exists
    >>> if os.path.exists('afds114_sub009_t2r1.nii'):
    ...     os.unlink('afds114_sub009_t2r1.nii')  # delete file

.. nbplot::

    >>> #: import initilization of nipype / MATLAB interface from "introducing
    >>> #  nipype" page.
    >>> import nipype_settings

.. nbplot::

    >>> #: import slice timing from nipype SPM interfaces
    >>> from nipype.interfaces.spm import SliceTiming

Your job is to create the ``SliceTiming`` SPM batch job from the parameters
you need.

Hints:

* try using IPython to look for help on the ``SliceTiming`` object;
* use the ``help`` methods for ``SliceTiming`` with ``SliceTiming.help()``;
* create a ``SliceTiming`` instances (`st = SliceTiming()``) and use IPython
  to look for help the inputs you need at `st.inputs`;

.. nbplot::

    >>> #- Initialize the SliceTiming batch object, and fill parameters
    >>> #- Run the slice timing on the fixed image `fds114_sub009_t2r1.nii`
    >>> st = SliceTiming()
    >>> st.inputs.in_files = 'fds114_sub009_t2r1.nii'
    >>> st.inputs.num_slices = num_slices
    >>> st.inputs.time_repetition = TR
    >>> st.inputs.time_acquisition = TA
    >>> st.inputs.slice_order = acq_order
    >>> st.inputs.ref_slice = 1

.. nbplot::
    :run-parts: 0 if have_spm else ()

    >>> #- Run the batch job
    >>> st.run()
    <nipype.interfaces.base.InterfaceResult object at ...>

Check that you did write a new slice-time corrected file into the current
directory.

.. solution-start

.. nbplot::
    :run-parts: 0 if have_spm else ()

    >>> # check for file created by nipype slice timing
    >>> assert os.path.exists('afds114_sub009_t2r1.nii')

.. solution-end
