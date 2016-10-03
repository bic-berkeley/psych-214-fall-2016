############
Numpy arange
############

``arange`` in NumPy is very like the Python :ref:`ranges` callable with two
important differences:

* ``arange`` returns an array rather than a ``range`` object (Python 3) or a
  list (Python 2);
* ``arange`` arguments can be floating point values.

.. nbplot::

    >>> import numpy as np

    >>> np.arange(4, 11, 2)
    array([ 4,  6,  8, 10])
    >>> np.arange(4, 11, 0.5)
    array([  4. ,   4.5,   5. ,   5.5,   6. ,   6.5,   7. ,   7.5,   8. ,
             8.5,   9. ,   9.5,  10. ,  10.5])

Because ``arange`` returns arrays, you can use NumPy element-wise operations
to multiply by the step size and add a start value.  This is one way to create
equally spaced vectors (``np.linspace`` is another):

.. nbplot::

    >>> np.arange(10) * 0.5 + 4
    array([ 4. ,  4.5,  5. ,  5.5,  6. ,  6.5,  7. ,  7.5,  8. ,  8.5])
