arr_1d_bigger = np.arange(24)
arr_1d_bigger
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
# 17, 18, 19, 20, 21, 22, 23])
arr_1d_bigger.shape
# (24,)
arr_3d = arr_1d_bigger.reshape((2, 3, 4))
arr_3d
# array([[[ 0,  1,  2,  3],
# [ 4,  5,  6,  7],
# [ 8,  9, 10, 11]],
# <BLANKLINE>
# [[12, 13, 14, 15],
# [16, 17, 18, 19],
# [20, 21, 22, 23]]])
