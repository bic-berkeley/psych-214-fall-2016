###########################
Indexing with boolean masks
###########################

.. testsetup::

    import numpy as np
    np.set_printoptions(precision=6)  # Only show 6 decimals when printing
    import matplotlib.pyplot as plt

.. nbplot::

    >>> # - import common modules
    >>> import numpy as np  # the Python array package
    >>> import matplotlib.pyplot as plt  # the Python plotting package

First we make a 3D array of shape (4, 3, 2)

.. nbplot::

    >>> slab0 = np.reshape(np.arange(12), (4, 3))
    >>> slab0
    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [ 9, 10, 11]])

.. nbplot::

    >>> slab1 = np.reshape(np.arange(100, 112), (4, 3))
    >>> slab1
    array([[100, 101, 102],
           [103, 104, 105],
           [106, 107, 108],
           [109, 110, 111]])

.. nbplot::

    >>> arr_3d = np.zeros((4, 3, 2))
    >>> arr_3d[:, :, 0] = slab0
    >>> arr_3d[:, :, 1] = slab1
    >>> arr_3d
    array([[[   0.,  100.],
            [   1.,  101.],
            [   2.,  102.]],
    <BLANKLINE>
           [[   3.,  103.],
            [   4.,  104.],
            [   5.,  105.]],
    <BLANKLINE>
           [[   6.,  106.],
            [   7.,  107.],
            [   8.,  108.]],
    <BLANKLINE>
           [[   9.,  109.],
            [  10.,  110.],
            [  11.,  111.]]])

We can index this with a one-dimensional boolean array. This selects
elements from the first axis.

.. nbplot::

    >>> bool_1d = np.array([False, True, True, False])
    >>> arr_3d[bool_1d]
    array([[[   3.,  103.],
            [   4.,  104.],
            [   5.,  105.]],
    <BLANKLINE>
           [[   6.,  106.],
            [   7.,  107.],
            [   8.,  108.]]])

We can also index with a two-dimensional boolean array, this selects elements
from the first two axes.

.. nbplot::

    >>> bool_2d = np.array([[False, True, False],
    ...                     [True, False, True],
    ...                     [True, False, False],
    ...                     [False, False, True],
    ...                    ])
    >>> bool_2d
    array([[False,  True, False],
           [ True, False,  True],
           [ True, False, False],
           [False, False,  True]], dtype=bool)

.. nbplot::

    >>> arr_3d[bool_2d]
    array([[   1.,  101.],
           [   3.,  103.],
           [   5.,  105.],
           [   6.,  106.],
           [  11.,  111.]])

We can even index with a 3D array, this selects elements over all three
dimensions.  In which order does it get the elements?

.. nbplot::

    >>> arr_is_odd = (arr_3d % 2) == 1
    >>> arr_is_odd
    array([[[False, False],
            [ True,  True],
            [False, False]],
    <BLANKLINE>
           [[ True,  True],
            [False, False],
            [ True,  True]],
    <BLANKLINE>
           [[False, False],
            [ True,  True],
            [False, False]],
    <BLANKLINE>
           [[ True,  True],
            [False, False],
            [ True,  True]]], dtype=bool)
    >>> arr_3d[arr_is_odd]
    array([   1.,  101.,    3.,  103.,    5.,  105.,    7.,  107.,    9.,
            109.,   11.,  111.])

We can mix 1D boolean arrays with ordinary slicing to select elements on
a single axis.

.. nbplot::

    >>> bool_1d_dim3 = np.array([False, True])
    >>> arr_3d[:, :, bool_1d_dim3]
    array([[[ 100.],
            [ 101.],
            [ 102.]],
    <BLANKLINE>
           [[ 103.],
            [ 104.],
            [ 105.]],
    <BLANKLINE>
           [[ 106.],
            [ 107.],
            [ 108.]],
    <BLANKLINE>
           [[ 109.],
            [ 110.],
            [ 111.]]])
