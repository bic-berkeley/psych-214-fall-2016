#- Your "mt_hrf" function here
def mt_hrf(times):
    """ Return values for HRF at given times """
    # Gamma pdf for the peak
    peak_values = gamma.pdf(times, 7)
    # Gamma pdf for the undershoot
    undershoot_values = gamma.pdf(times, 20)
    # Combine them
    values = peak_values - undershoot_values
    # Scale max to 0.6
    return values / np.max(values) * 0.6
