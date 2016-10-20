# Show what arrays NumPy will broadcast to.
bc_arr, bc_row_means = np.broadcast_arrays(arr, row_means_col_vec)
# The (4, 3) array is unchanged when broadcasting.
np.all(bc_arr == arr)
# True
# The (4, 1) array has its columns replicated to give a (4, 3) array.
bc_row_means
# array([[ 2.666667,  2.666667,  2.666667],
# [ 5.      ,  5.      ,  5.      ],
# [ 4.333333,  4.333333,  4.333333],
# [ 5.333333,  5.333333,  5.333333]])
