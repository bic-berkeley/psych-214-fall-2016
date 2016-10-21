import numpy as np
import matplotlib.pyplot as plt
# Print array values to 4 decimal places
np.set_printoptions(precision=4)

import nibabel as nib
img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
data = data[..., 4:]
