#################################
Random numbers with ``np.random``
#################################

.. nbplot::

    >>> #: standard imports
    >>> import numpy as np
    >>> # print arrays to 4 decimal places
    >>> np.set_printoptions(precision=4, suppress=True)

.. nbplot::
    :include-source: false

    >>> np.random.seed(1966)

We often need random numbers, for tests and for taking random samples, and for
other things. ``np.random`` is a submmodule within numpy:

.. nbplot::

    >>> type(np.random)
    <class 'module'>

It has a set of functions for returning random numbers of various sorts.  For
example, to return a single random number from the default normal distribution
(mean 0, variance 1):

.. nbplot::

    >>> np.random.normal()
    -1.7834767234872053

You can set the mean and variance with the first two input parameters:

.. nbplot::

    >>> # Random number from distribution with mean 15, variance 2
    >>> np.random.normal(15, 2)
    16.428500754488095

To return a 8 by 5 array of random numbers from the same distribution:

.. nbplot::

    >>> np.random.normal(15, 2, size=(8, 5))
    array([[ 14.1012,  13.8795,  14.9896,  14.68  ,  16.7738],
           [ 15.6412,  15.1879,  16.0879,  18.1683,  15.5654],
           [ 14.0215,  14.1252,  15.7508,  22.9831,  14.2049],
           [ 18.7052,  14.4397,  16.8221,  14.057 ,  15.8822],
           [ 18.0949,  13.8383,  16.7131,  18.4536,  13.9215],
           [ 16.673 ,  13.9692,  12.2647,  14.165 ,  13.4826],
           [ 15.4742,  16.2787,  16.6687,  18.4134,  13.5539],
           [ 14.5237,  14.8205,  13.9509,  13.5294,  13.4682]])

A 5 by 3 array of random numbers from the standard normal distribution with
mean 1 and variance 1:

.. nbplot::

    >>> np.random.normal(size=(8, 5))
    array([[ 2.5219,  0.3761,  1.5856, -2.2039, -0.0235],
           [ 0.3361,  0.1054,  1.5067,  0.4116, -0.1222],
           [ 0.3571, -1.9315, -1.0591,  1.1355,  1.1751],
           [-0.993 ,  0.5273,  1.8294,  0.0017,  0.3562],
           [ 0.2322,  0.7887,  0.7868,  0.2953,  1.0391],
           [ 0.2471,  0.1886, -1.387 , -1.5353, -0.1975],
           [ 1.164 ,  0.9484,  1.6722,  0.6664, -0.7618],
           [-0.1857, -0.8744, -0.0779,  0.9732,  0.0364]])

*********************************
Making random numbers predictable
*********************************

Sometimes you want to make sure that the random numbers are predictable, in
that you will always get the same set of random numbers from a series of calls
to the ``numpy.random`` functions.  You can achieve this by giving the random
numbers a *seed*.  This is an integer that sets the random number generator
into a predictable state, such that it will always return the same sequence of
random numbers from this point:

.. nbplot::

    >>> # Set the state of the random number generator
    >>> np.random.seed(42)
    >>> # One set of random numbers
    >>> first_random_arr = np.random.normal(size=(4, 2))
    >>> first_random_arr
    array([[ 0.4967, -0.1383],
           [ 0.6477,  1.523 ],
           [-0.2342, -0.2341],
           [ 1.5792,  0.7674]])
    >>> # Another set
    >>> second_random_arr = np.random.normal(size=(4, 2))
    >>> second_random_arr
    array([[-0.4695,  0.5426],
           [-0.4634, -0.4657],
           [ 0.242 , -1.9133],
           [-1.7249, -0.5623]])
    >>> # Reset the state of the random number generator
    >>> np.random.seed(42)
    >>> # The same as "first_random_arr" above.
    >>> np.random.normal(size=(4, 2))
    array([[ 0.4967, -0.1383],
           [ 0.6477,  1.523 ],
           [-0.2342, -0.2341],
           [ 1.5792,  0.7674]])
    >>> # The same as "second_random_arr" above.
    >>> np.random.normal(size=(4, 2))
    array([[-0.4695,  0.5426],
           [-0.4634, -0.4657],
           [ 0.242 , -1.9133],
           [-1.7249, -0.5623]])
