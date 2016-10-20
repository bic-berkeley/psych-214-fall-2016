# Fill in a NumPy array
import numpy as np
numbers = np.arange(24)
py_arr = np.zeros((2, 3, 4))
n_index = 0  # Python has 0-based indices
for i in range(2):  # row index changes slowest
    for j in range(3):  # then column index
        for k in range(4):  # depth index changes fastest
            py_arr[i, j, k] = numbers[n_index];
            n_index += 1
# ...
print(py_arr[:, :, 0])
# [[  0.   4.   8.]
# [ 12.  16.  20.]]
print(py_arr[:, :, 1])
# [[  1.   5.   9.]
# [ 13.  17.  21.]]
