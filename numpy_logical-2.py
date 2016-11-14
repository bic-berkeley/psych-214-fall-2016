import numpy as np

bool1 = np.array([True, True, False, False])
bool2 = np.array([False, True, False, True])

bool1 and bool2
# Traceback (most recent call last):
# ...
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

bool1 or bool2
# Traceback (most recent call last):
# ...
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
