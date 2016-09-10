# First axis first fetching, like MATLAB
first_1_reshaped = numbers.reshape((2, 3, 4), order='F')
print(first_1_reshaped[:, :, 0])
# [[0 2 4]
# [1 3 5]]
print(first_1_reshaped[:, :, 1])
# [[ 6  8 10]
# [ 7  9 11]]
