#: import the gamma probability density function
from scipy.stats import gamma
# >>>
def mt_hrf(times):
    """ Return values for HRF at given times
# ...
    This is the "not_great_hrf" from the "make_an_hrf" exercise.
    """
    # Gamma pdf for the peak
    peak_values = gamma.pdf(times, 6)
    # Gamma pdf for the undershoot
    undershoot_values = gamma.pdf(times, 12)
    # Combine them
    values = peak_values - 0.35 * undershoot_values
    # Scale max to 0.6
    return values / np.max(values) * 0.6
