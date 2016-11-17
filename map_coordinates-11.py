# Resample using map_coordinates
from scipy.ndimage import map_coordinates
resampled_mean_again = map_coordinates(mean_bold_data,
                                       coords_first_again)
