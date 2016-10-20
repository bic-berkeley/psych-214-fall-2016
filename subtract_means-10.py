# Make row_means into column vector so numpy knows to replicate
# the columns during broadcasting.
row_means_col_vec = row_means.reshape((4, 1))  # Better: np.newaxis.
broadcast_demeaned = arr - row_means_col_vec
broadcast_demeaned.mean(axis=1)
# array([ 0.,  0.,  0.,  0.])
