""" Predicted neural time course exercise
"""
#: compatibility with Python 2
from __future__ import print_function, division

#: Standard imports
import numpy as np
import matplotlib.pyplot as plt
# Print arrays to 4 decimal places
np.set_printoptions(precision=4, suppress=True)

#- Load the image with nibabel.
#- Get the image data array, print the data shape.

#: Read in stimulus file, return neural prediction
def events2neural(task_fname, tr, n_trs):
    """ Return predicted neural time course from event file

    Parameters
    ----------
    task_fname : str
        Filename of event file
    tr : float
        TR in seconds
    n_trs : int
        Number of TRs in functional run

    Returns
    -------
    time_course : array shape (n_trs,)
        Predicted neural time course, one value per TR
    """
    task = np.loadtxt(task_fname)
    if task.ndim != 2 or task.shape[1] != 3:
        raise ValueError("Is {0} really a task file?", task_fname)
    task[:, :2] = task[:, :2] / tr
    time_course = np.zeros(n_trs)
    for onset, duration, amplitude in task:
        onset, duration = int(onset),  int(duration)
        time_course[onset:onset + duration] = amplitude
    return time_course

#: TR for this run
tr = 2.5

#- Read the stimulus data file and return a predicted neural time
#- course.
#- Plot the predicted neural time course.

#- Make new array excluding the first volume
#- data_no_0 = ?

#- Knock the first element off the neural prediction time series.
#- neural_prediction_no_0 = ?

#: subtracting rest from task scans
task_scans = data_no_0[..., neural_prediction_no_0 == 1]
rest_scans = data_no_0[..., neural_prediction_no_0 == 0]
difference = task_scans.mean(axis=-1) - rest_scans.mean(axis=-1)

#: showing slice 14 from the difference image
plt.imshow(difference[:, :, 14], cmap='gray')

#- Get the values for (i, j, k) = (45, 43, 14) and every volume.
#- Plot the values (voxel time course).

#- Correlation of predicted neural time course with voxel signal time
#- course

#: import the gamma probability density function
from scipy.stats import gamma

def mt_hrf(times):
    """ Return values for HRF at given times

    This is the "not_great_hrf" from the "make_an_hrf" exercise.
    Feel free to replace this function with your improved version from
    that exercise.
    """
    # Gamma pdf for the peak
    peak_values = gamma.pdf(times, 6)
    # Gamma pdf for the undershoot
    undershoot_values = gamma.pdf(times, 12)
    # Combine them
    values = peak_values - 0.35 * undershoot_values
    # Scale max to 0.6
    return values / np.max(values) * 0.6

#- Make a vector of times at which to sample the HRF

#- Sample HRF at given times
#- Plot HRF samples against times

#- Convolve predicted neural time course with HRF samples

#- Remove extra tail of values put there by the convolution

#- Plot convolved neural prediction and unconvolved neural prediction

#- Correlation of the convolved time course with voxel time course

#- Scatterplot the hemodynamic prediction against the signal
