############################
Slicing with boolean vectors
############################

We have already seen how to slice arrays using colons and integers.

The colon means 'all the elements on this axis':

.. nbplot::

    >>> import numpy as np
    >>> an_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
    >>> # All rows, only the second column
    >>> an_array[:, 1]
    array([1, 5])

    >>> # Only the first row, all columns except the first
    >>> an_array[0, 1:]
    array([1, 2, 3])

We have also seen how to slice using a boolean array the same shape as the
original:

.. nbplot::

    >>> is_gt_5 = an_array > 5
    >>> is_gt_5
    array([[False, False, False, False],
           [False, False,  True,  True]], dtype=bool)

    >>> # Select elements greater than 5 into 1D array
    >>> an_array[is_gt_5]
    array([6, 7])

We can also use boolean vectors to select elements on a particular axis.  So,
for example, let's say we want the first and last elements on the second axis.
We can use a boolean vector to select these elements from a particular axis,
while still using integer and colon syntax for the other axes:

.. nbplot::

    >>> want_first_last = np.array([True, False, False, True])

    >>> # All rows, columns as identified by boolean vector
    >>> an_array[:, want_first_last]
    array([[0, 3],
           [4, 7]])
