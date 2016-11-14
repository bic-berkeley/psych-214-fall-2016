arr_is_odd = (arr_3d % 2) == 1
arr_is_odd
# array([[[False, False],
# [ True,  True],
# [False, False]],
# <BLANKLINE>
# [[ True,  True],
# [False, False],
# [ True,  True]],
# <BLANKLINE>
# [[False, False],
# [ True,  True],
# [False, False]],
# <BLANKLINE>
# [[ True,  True],
# [False, False],
# [ True,  True]]], dtype=bool)
arr_3d[arr_is_odd]
# array([   1.,  101.,    3.,  103.,    5.,  105.,    7.,  107.,    9.,
# 109.,   11.,  111.])
