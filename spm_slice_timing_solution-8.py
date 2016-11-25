# - generate acq_order list
odd = range(1, num_slices+1, 2)
even = range(2, num_slices+1, 2)
acq_order = list(odd) + list(even)
acq_order
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
