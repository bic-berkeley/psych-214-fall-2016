""" Making our own hemodynamic response function
"""
#: compatibility with Python 2
from __future__ import print_function, division

#: Import array and plotting libraries.
import numpy as np
import matplotlib.pyplot as plt
# Print arrays to 4 decimal places
np.set_printoptions(precision=4, suppress=True)

#- Load the estimated values from the text file into an array
#- Make an array of corresponding times
#- Plot signal by time

#: import the gamma density function
from scipy.stats import gamma

#: my attempt - you can do better than this
def not_great_hrf(times):
    """ Return values for HRF at given times """
    # Gamma pdf for the peak
    peak_values = gamma.pdf(times, 6)
    # Gamma pdf for the undershoot
    undershoot_values = gamma.pdf(times, 12)
    # Combine them
    values = peak_values - 0.35 * undershoot_values
    # Scale max to 0.6
    return values / np.max(values) * 0.6

#: plot the data against my estimate
plt.plot(mt_hrf_times, not_great_hrf(mt_hrf_times), label='not_great_hrf')
plt.plot(mt_hrf_times, mt_hrf_estimates, label='mt_hrf_estimates')
plt.legend()

#- Your "mt_hrf" function here

#- Plot your function against the mt_hrf_estimates data to test

#- Evidence that your function is better than mine?
