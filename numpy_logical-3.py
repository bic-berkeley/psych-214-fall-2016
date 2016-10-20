# "logical_and" True where both of bool1 and bool2 are True
np.logical_and(bool1, bool2)
# array([False,  True, False, False], dtype=bool)

# "logical_or" True where either of bool1 and bool2 are True
np.logical_or(bool1, bool2)
# array([ True,  True, False,  True], dtype=bool)

# "logical_not" True where input array is False
np.logical_not(bool1)
# array([False, False,  True,  True], dtype=bool)
