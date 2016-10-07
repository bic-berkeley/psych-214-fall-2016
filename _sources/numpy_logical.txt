************************************
Logical operations on boolean arrays
************************************

``np.logical_and``, ``np.logical_or``:

Sometimes we want to combine boolean values using logical operators like AND,
OR, NOT.  This is straightforward for Python booleans:

.. nbplot::

    >>> # Logical AND - True only if both are True
    >>> True and True
    True
    >>> True and False
    False

    >>> # Logical OR - True if either or both are True
    >>> True or True
    True
    >>> True or False
    True
    >>> False or False
    False

    >>> # Logical NOT - inverts truth value
    >>> not True
    False
    >>> not False
    True

We have to do a little more work for *arrays* of booleans, because the Python
``and``, ``or``, ``not`` operators only return a single boolean values, and so
do not operate as we expect on arrays:

.. nbplot::

    >>> import numpy as np

    >>> bool1 = np.array([True, True, False, False])
    >>> bool2 = np.array([False, True, False, True])

    >>> bool1 and bool2
    Traceback (most recent call last):
       ...
    ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

    >>> bool1 or bool2
    Traceback (most recent call last):
       ...
    ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

To do elementwise AND, OR, NOT, we can use ``np.logical_and, np.logical_or,
np.logical_not``:

.. nbplot::

    >>> # "logical_and" True where both of bool1 and bool2 are True
    >>> np.logical_and(bool1, bool2)
    array([False,  True, False, False], dtype=bool)

    >>> # "logical_or" True where either of bool1 and bool2 are True
    >>> np.logical_or(bool1, bool2)
    array([ True,  True, False,  True], dtype=bool)

    >>> # "logical_not" True where input array is False
    >>> np.logical_not(bool1)
    array([False, False,  True,  True], dtype=bool)
