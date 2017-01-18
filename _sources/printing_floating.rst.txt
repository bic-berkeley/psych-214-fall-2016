###########################################
Making floating points numbers print nicely
###########################################

By default, when numpy prints an array, it looks for very small or very large
numbers. If it finds either, it uses exponents to show the numbers. This can
be annoying:

.. nbplot::
    :include-source: false

    >>> import numpy as np
    >>> np.set_printoptions(precision=8, suppress=False)

.. nbplot::

    >>> import numpy as np
    >>> np.pi
    3.141592653589793

.. nbplot::

    >>> np.array([np.pi, 0.000001])
    array([  3.14159265e+00,   1.00000000e-06])

In order to avoid this, you can tell numpy not to use exponential notation for
small numbers:

.. nbplot::

    >>> np.set_printoptions(suppress=True)
    >>> np.array([np.pi, 0.000001])
    array([ 3.14159265,  0.000001  ])

This setting stays in place until you change it:

.. nbplot::

    >>> np.array([np.pi, 0.000001])
    array([ 3.14159265,  0.000001  ])

It can also be annoying to see many digits after the decimal point, if
you know that these are not important. You can set the number of digits
after the decimal point for numpy printing like this:

.. nbplot::

    >>> np.set_printoptions(precision=4)
    >>> a = np.array([np.pi, 0.000001])
    >>> a
    array([ 3.1416,  0.    ])

This only affects printing, not calculations:

.. nbplot::

    >>> b = a * 2
    >>> b
    array([ 6.2832,  0.    ])
    >>> # change the printoptions again, we see more decimal places
    >>> np.set_printoptions(precision=8)
    >>> b
    array([ 6.28318531,  0.000002  ])
