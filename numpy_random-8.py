# Set the state of the random number generator
np.random.seed(42)
# One set of random numbers
first_random_arr = np.random.normal(size=(4, 2))
first_random_arr
# array([[ 0.4967, -0.1383],
# [ 0.6477,  1.523 ],
# [-0.2342, -0.2341],
# [ 1.5792,  0.7674]])
# Another set
second_random_arr = np.random.normal(size=(4, 2))
second_random_arr
# array([[-0.4695,  0.5426],
# [-0.4634, -0.4657],
# [ 0.242 , -1.9133],
# [-1.7249, -0.5623]])
# Reset the state of the random number generator
np.random.seed(42)
# The same as "first_random_arr" above.
np.random.normal(size=(4, 2))
# array([[ 0.4967, -0.1383],
# [ 0.6477,  1.523 ],
# [-0.2342, -0.2341],
# [ 1.5792,  0.7674]])
# The same as "second_random_arr" above.
np.random.normal(size=(4, 2))
# array([[-0.4695,  0.5426],
# [-0.4634, -0.4657],
# [ 0.242 , -1.9133],
# [-1.7249, -0.5623]])
