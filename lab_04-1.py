import numpy as np

bool1 = np.array([True, True, False, False])
bool2 = np.array([False, True, False, True])

# logical_and True where both of bool1 and bool2 are True
np.logical_and(bool1, bool2)
# array([False,  True, False, False], dtype=bool)

# logical_or True where either of bool1 and bool2 are True
np.logical_or(bool1, bool2)
# array([ True,  True, False,  True], dtype=bool)
