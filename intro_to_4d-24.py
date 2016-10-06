tf_lt_10 = first_vol < 10
vals_lt_10 = first_vol[tf_lt_10]
np.unique(vals_lt_10)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int16)
