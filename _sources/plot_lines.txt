############################
Plotting lines in matplotlib
############################

.. nbplot::
    :include-source: false

    >>> # - compatibility with Python 2
    >>> from __future__ import print_function
    >>> from __future__ import division

.. nbplot::

    >>> import matplotlib.pyplot as plt

To plot a line in matplotlib, use ``plot`` with the X coordinates as the first
argument and the matching Y coordinates as the second argument:

.. nbplot::

    >>> # A line from (1, 2) to (7, 11)
    >>> plt.plot([1, 7], [2, 11])
    [...]
    >>> # Another line from (2, 6) to (8, 1)
    >>> plt.plot([2, 8], [6, 1])
    [...]
