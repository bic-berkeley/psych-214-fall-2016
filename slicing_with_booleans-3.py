want_first_last = np.array([True, False, False, True])

# All rows, columns as identified by boolean vector
an_array[:, want_first_last]
# array([[0, 3],
# [4, 7]])
