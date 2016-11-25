#: Full-width at half-maximum to sigma
def fwhm2sigma(fwhm):
    return fwhm / np.sqrt(8 * np.log(2))
