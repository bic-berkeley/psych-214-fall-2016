.. vim:ft=rst

#####################################
Making a predicted neural time course
#####################################

.. nbplot::
    :include-source: false

    >>> #: compatibility with Python 2
    >>> from __future__ import print_function, division

.. nbplot::

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt

We are going to be analyzing the data for the 4D image
:download:`ds114_sub009_t2r1.nii` again.

Load the image into an image object with nibabel, and get the image data
array. Print the shape.

.. nbplot::

    >>> #- Load the image with nibabel.
    >>> #- Get the image data array, print the data shape.
    >>> import nibabel as nib
    >>> img = nib.load('ds114_sub009_t2r1.nii')
    >>> data = img.get_data()
    >>> data.shape
    (64, 64, 30, 173)

Next we read in the stimulus file for this run to make an on - off
time-series.

The stimulus file is :download:`ds114_sub009_t2r1_cond.txt`.

Here's a version of the same thing we did in an earlier exercise, as a
function:

.. nbplot::

    >>> #: Read in stimulus file, return neural prediction
    >>> def events2neural(task_fname, tr, n_trs):
    ...     """ Return predicted neural time course from event file
    ...
    ...     Parameters
    ...     ----------
    ...     task_fname : str
    ...         Filename of event file
    ...     tr : float
    ...         TR in seconds
    ...     n_trs : int
    ...         Number of TRs in functional run
    ...
    ...     Returns
    ...     -------
    ...     time_course : array shape (n_trs,)
    ...         Predicted neural time course, one value per TR
    ...     """
    ...     task = np.loadtxt(task_fname)
    ...     if task.ndim != 2 or task.shape[1] != 3:
    ...         raise ValueError("Is {0} really a task file?", task_fname)
    ...     task[:, :2] = task[:, :2] / tr
    ...     time_course = np.zeros(n_trs)
    ...     for onset, duration, amplitude in task:
    ...         time_course[onset:onset + duration] = amplitude
    ...     return time_course

Use this function to read ``ds114_sub009_t2r1_cond.txt`` and return a
predicted neural time course.

The TR for this run is 2.5. You know the number of TRs from the image
data shape above.

.. nbplot::

    >>> #- Read the stimulus data file and return a predicted neural time
    >>> #- course.
    >>> #- Plot the predicted neural time course.
    >>> tr = 2.5
    >>> neural_prediction = events2neural('ds114_sub009_t2r1_cond.txt', tr, data.shape[-1])
    >>> plt.plot(neural_prediction)
    >>> plt.ylim(0, 1.2)
    (0, 1.2)

We had previously found that the first volume in this run was bad. Use your
slicing skills to make a new array called ``data_no_0`` that is the data array
without the first volume:

.. nbplot::

    >>> #- Make new array excluding the first volume
    >>> #- data_no_0 = ?
    >>> data_no_0 = data[..., 1:]

Our neural prediction time series currently has one value per volume,
including the first volume. To match the data, make a new neural prediction
variable that does not include the first value of the time series. Call this
new variable ``neural_prediction_no_0``.

.. nbplot::

    >>> #- Knock the first element off the neural prediction time series.
    >>> #- neural_prediction_no_0 = ?
    >>> neural_prediction_no_0 = neural_prediction[1:]

For now, we're going to play with data for a single voxel.

In an earlier exercise, we subtracted the rest scans from the task scans,
something like this:

.. nbplot::

    >>> #: subtracting rest from task scans
    >>> task_scans = data_no_0[..., neural_prediction_no_0 == 1]
    >>> rest_scans = data_no_0[..., neural_prediction_no_0 == 0]
    >>> difference = np.mean(task_scans, axis=-1) - np.mean(rest_scans, axis=-1)

.. nbplot::

    >>> #: showing slice 14 from the difference image
    >>> plt.imshow(difference[:, :, 14], cmap='gray')
    <...>

It looks like there's a voxel that is greater for activation than rest at
about (i, j, k) == (45, 43, 14).

Get and plot the values for this voxel position, for every volume in the 4D
data (not including the first volume). You can do it with a loop, but slicing
is much nicer.

.. nbplot::

    >>> #- Get the values for (i, j, k) = (45, 43, 14) and every volume.
    >>> #- Plot the values (voxel time course).
    >>> voxel_values = data_no_0[45, 43, 14, :]
    >>> plt.plot(voxel_values)
    [...]

Correlate the predicted neural time series with the voxel time course:

.. nbplot::

    >>> #- Correlation of predicted neural time course with voxel signal time
    >>> #- course
    >>> np.corrcoef(neural_prediction_no_0, voxel_values)
    array([[ 1.        ,  0.31166306],
           [ 0.31166306,  1.        ]])

Now we will do a predicted hemodynamic time course using convolution.

Next we need to get the HRF vector to convolve with.

Remember we have defined the HRF as a function of time, not TRs.

For our convolution, we need to *sample* the HRF at times corresponding the
start of the TRs.

So, we need to sample at times (0, 2.5, ...)

Make a vector of times at which to sample the HRF. We want to sample every TR
up until (but not including) somewhere near 35 seconds (where the HRF should
have got close to zero again).

.. nbplot::

    >>> #- Make a vector of times at which to sample the HRF
    >>> hrf_times = np.arange(0, 35, tr)
    >>> hrf_times
    array([  0. ,   2.5,   5. ,   7.5,  10. ,  12.5,  15. ,  17.5,  20. ,
            22.5,  25. ,  27.5,  30. ,  32.5])

Sample your HRF function at these times and plot:

.. nbplot::

    >>> #- Sample HRF at given times
    >>> #- Plot HRF samples against times
    >>> hrf_signal = mt_hrf(hrf_times)
    >>> plt.plot(hrf_times, hrf_signal)
    [...]

Convolve the predicted neural time course with the HRF samples:

.. nbplot::

    >>> #- Convolve predicted neural time course with HRF samples
    >>> hemodynamic_prediction = np.convolve(neural_prediction_no_0, hrf_signal)

The default output of convolve is longer than the input neural prediction
vector, by the length of the convolving vector (the HRF samples) minus 1.
Knock these last values off the result of the convolution to get a vector the
same length as the neural prediction:

.. nbplot::

    >>> #- Remove extra tail of values put there by the convolution
    >>> hemodynamic_prediction = hemodynamic_prediction[:len(neural_prediction_no_0)]

Plot the convolved neural prediction, and then, on the same plot, plot the
unconvolved neural prediction.

.. nbplot::

    >>> #- Plot convolved neural prediction and unconvolved neural prediction
    >>> plt.plot(neural_prediction, label='unconvolved')
    [...]
    >>> plt.plot(hemodynamic_prediction, label='convolved')
    [...]
    >>> plt.legend()
    <...>

Does the new convolved time course correlate better with the voxel time
course?

.. nbplot::

    >>> #- Correlation of the convolved time course with voxel time course
    >>> np.corrcoef(hemodynamic_prediction, voxel_values)
    array([[ 1.        ,  0.33029022],
           [ 0.33029022,  1.        ]])

Plot the hemodynamic prediction against the actual signal (voxel values).
Remember to use a marker such as '+' to give you a scatter plot. How does it
look?

.. nbplot::

    >>> #- Scatterplot the hemodynamic prediction against the signal
    >>> plt.plot(hemodynamic_prediction, voxel_values, '+')
    >>> plt.xlabel('hemodynamic prediction')
    >>> plt.ylabel('voxel values')
    <...>
