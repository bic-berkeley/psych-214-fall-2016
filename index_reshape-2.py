numbers = np.arange(24)
reshaped = numbers.reshape((2, 3, 4))
# This is exactly the same as the original ``py_arr``
np.all(reshaped == py_arr)
# True
