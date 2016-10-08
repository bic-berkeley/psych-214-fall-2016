#########################################
Testing for near equality with "allclose"
#########################################

When the computer calculates a floating point value, there will often be some
degree of error in the calculation, because the computer floating point format
cannot represent every floating point number exactly. See:

* `floating point`_;
* `floating point error`_.

When we check the results of a floating point calculation, we often want to
avoid checking if the returned value is exactly equal to a desired value.
Rather, we want to check whether the returned value is close enough, given the
usual floating point error.  A common idiom in NumPy is to use the
``np.allclose`` function, which checks whether two values or two arrays are
equal, within a small amount of error:

.. nbplot::

    >>> import numpy as np

    >>> np.pi == 3.1415926
    False
    >>> # pi to 7 decimal places not exactly equal to pi
    >>> np.allclose(np.pi, 3.1415926)
    True
    >>> # pi to 7 dp is "close" to pi
    >>> np.allclose([np.pi, 2 * np.pi], [3.1415926, 6.2831852])
    True

See the docstring for ``np.allclose`` for details of what "close" means.
