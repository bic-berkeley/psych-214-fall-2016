import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
# Only show 6 decimals when printing
np.set_printoptions(precision=6)

img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
data = data[..., 4:]
