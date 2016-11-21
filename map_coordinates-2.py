#: standard imports
import numpy as np
import numpy.linalg as npl
# print arrays to 4 decimal places
np.set_printoptions(precision=4, suppress=True)
import matplotlib.pyplot as plt
#: gray colormap and nearest neighbor interpolation by default
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'nearest'
import nibabel as nib
