import numpy as np

np.pi == 3.1415926
# False
# pi to 7 decimal places not exactly equal to pi
np.allclose(np.pi, 3.1415926)
# True
# pi to 7 dp is "close" to pi
np.allclose([np.pi, 2 * np.pi], [3.1415926, 6.2831852])
# True
