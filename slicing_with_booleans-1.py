import numpy as np
an_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
# All rows, only the second column
an_array[:, 1]
# array([1, 5])

# Only the first row, all columns except the first
an_array[0, 1:]
# array([1, 2, 3])
