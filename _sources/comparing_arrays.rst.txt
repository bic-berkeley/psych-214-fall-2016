################
Comparing arrays
################

A comparison between two arrays returns the *elementwise* result of the
comparison:

.. nbplot::

    >>> import numpy as np
    >>> arr1 = np.array([[0, 1, 2],
    ...                 [3, 4, 5]])
    >>> arr2 = np.array([[1, 1, 2],
    ...                  [3, 4, 6]])
    >>> arr1 == arr2
    array([[False,  True,  True],
           [ True,  True, False]], dtype=bool)

Sometimes we want to know if two arrays are equal, in the sense that all the
elements of the two arrays are equal to each other. For this we use
``np.all``. ``np.all`` accepts an array as input, and returns True if all the
elements are non-zero [#non-zero]_.

.. nbplot::

    >>> np.all([1, 2, 3])
    True

Python assumes that ``True == 1`` and ``False == 0`` for this test of
non-zero:

.. nbplot::

    >>> np.all([True, True, True])
    True

.. nbplot::

    >>> np.all([1, 2, 0])
    False
    >>> np.all([True, False, True])
    False

To ask whether all the elements in two arrays are equal, we can pass the
result of the element-wise comparison to ``np.all``:

.. nbplot::

    >>> np.all(arr1 == arr2)
    False

.. nbplot::

    >>> arr3 = arr1.copy()
    >>> np.all(arr1 == arr3)
    True

Sometimes we want to know if any of the values in an array are non-zero
[#non-zero]_.  Enter ``np.any``:

.. nbplot::

    >>> np.any([False, False, False])
    False

.. nbplot::

    >>> np.any([False, False, True])
    True

.. nbplot::

    >>> np.any(arr1 == arr2)
    True

.. nbplot::

    >>> np.any(arr1 != arr3)
    False

.. rubric:: Footnotes

.. [#non-zero] For numerical arrays, testing whether an element is "non-zero"
   has the obvious meaning of ``element != 0``.  For boolean arrays non-zero
   means ``element == True``.  For other array types, non-zero means
   ``bool(element) == True`` where ``bool`` uses the :ref:`equivalent-to-true`
   algorithm to return True or False from an element.
