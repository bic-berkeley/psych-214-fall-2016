is_gt_5 = an_array > 5
is_gt_5
# array([[False, False, False, False],
# [False, False,  True,  True]], dtype=bool)

# Select elements greater than 5 into 1D array
an_array[is_gt_5]
# array([6, 7])
