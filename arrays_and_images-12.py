old_shape = an_array.shape
a_1d_array = np.reshape(an_array, old_shape[0] * old_shape[1])
a_1d_array
# array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 99, 99, 94,  0,  0,
# 0,  0, 25, 99, 99, 79,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
# 0, 56, 99, 99, 49,  0,  0,  0,  0, 73, 99, 99, 31,  0,  0,  0,  0,
# 91, 99, 99, 13,  0,  0,  0,  9, 99, 99, 94,  0,  0,  0,  0, 27, 99,
# 99, 77,  0,  0,  0,  0, 45, 99, 99, 59,  0,  0,  0,  0, 63, 99, 99,
# 42,  0,  0,  0,  0, 80, 99, 99, 24,  0,  0,  0,  1, 96, 99, 99,  6,
# 0,  0,  0, 16, 99, 99, 88,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
# 0])