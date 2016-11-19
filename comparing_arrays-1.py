import numpy as np
arr1 = np.array([[0, 1, 2],
                [3, 4, 5]])
arr2 = np.array([[1, 1, 2],
                 [3, 4, 6]])
arr1 == arr2
# array([[False,  True,  True],
# [ True,  True, False]], dtype=bool)
