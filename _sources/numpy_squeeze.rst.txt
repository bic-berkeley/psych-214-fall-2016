#############################################
Removing length 1 axes with ``numpy.squeeze``
#############################################

Sometimes we find ourselves with arrays with length-1 axes - and we want to
remove these axes. For example:

.. nbplot::

    >>> import numpy as np
    >>> arr = np.random.normal(size=(4, 1, 6))
    >>> arr.shape
    (4, 1, 6)

.. nbplot::

    >>> squeezed = np.squeeze(arr)
    >>> squeezed.shape
    (4, 6)

.. nbplot::

    >>> arr = np.zeros((1, 3, 1, 7))
    >>> arr.shape
    (1, 3, 1, 7)

.. nbplot::

    >>> np.squeeze(arr).shape
    (3, 7)
