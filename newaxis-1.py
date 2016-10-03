import numpy as np

v = np.array([0, 3])
v.shape
# (2,)
# Insert a new length 1 dimension at the beginning
row_v = v[np.newaxis, :]
row_v.shape
# (1, 2)
row_v
# array([[0, 3]])
# Insert a new length 1 dimension at the end
col_v = v[:, np.newaxis]
col_v.shape
# (2, 1)
col_v
# array([[0],
# [3]])
