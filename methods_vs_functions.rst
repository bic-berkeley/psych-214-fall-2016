#############################
Methods vs functions in numpy
#############################

Many things are implemented in numpy as both *functions* and *methods*.  For
example, there is a ``np.sum`` function, that adds up all the elements:

.. nbplot::

    >>> import numpy as np

    >>> arr = np.array([1, 2, 0, 1])
    >>> np.sum(arr)
    4

There is also a ``sum`` method of the numpy ``array`` object:

.. nbplot::

    >>> type(arr)
    <class 'numpy.ndarray'>

.. nbplot::

    >>> arr.sum()
    4

Nearly all the method versions do the same thing as the function versions.
Examples are ``mean``, ``min``, ``max``, ``sum``, ``reshape``.  Choosing the
method or the function will usually depend on which one is easier to read.
