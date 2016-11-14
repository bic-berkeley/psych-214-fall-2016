import numpy as np
import matplotlib.pyplot as plt
cameraman = np.loadtxt('camera.txt').reshape((512, 512))
plt.imshow(cameraman.T, cmap='gray', interpolation='nearest')
# <...>
