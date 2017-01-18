######################################
Making coordinate arrays with meshgrid
######################################

:doc:`affine_transform <resampling_with_ndimage>` works by using voxel
coordinate implied by the ``output_shape``, and transforming those. See:
:ref:`implied-coordinate-grid`.

``numpy.meshgrid`` is a way of making an actual coordinate grid.

This is particularly useful when we want to use the more general form of image
resampling in ``scipy.ndimage.map_coordinates``.

If we have some shape |--| say ``output_shape`` |--| then this implies a set
of coordinates. Let's say ``output_shape = (5, 4)`` |--| implying a 2D array.

The implied coordinate grid will therefore have one coordinate for each pixel
(2D voxel) in the (5, 4) array.

Because this array is 2D, there are two coordinate values for each pixel. For
example, the coordinate of the first element in the array is (0, 0). We can
make these i- and j- coordinates with ``meshgrid``:

.. nbplot::

    >>> import numpy as np
    >>> i_coords, j_coords = np.meshgrid(range(5), range(4), indexing='ij')
    >>> i_coords
    array([[0, 0, 0, 0],
           [1, 1, 1, 1],
           [2, 2, 2, 2],
           [3, 3, 3, 3],
           [4, 4, 4, 4]])
    >>> j_coords
    array([[0, 1, 2, 3],
           [0, 1, 2, 3],
           [0, 1, 2, 3],
           [0, 1, 2, 3],
           [0, 1, 2, 3]])

We can make this into a shape (2, 5, 4) array where the first axis contains
the (i, j) coordinate.

.. nbplot::

    >>> coordinate_grid = np.array([i_coords, j_coords])
    >>> coordinate_grid.shape
    (2, 5, 4)

Because we have not done any transformation on the coordinate, the i, j
coordinate will be the same as the index we use to get the i, j coordinate:

.. nbplot::

    >>> coordinate_grid[:, 0, 0]
    array([0, 0])
    >>> coordinate_grid[:, 1, 0]
    array([1, 0])
    >>> coordinate_grid[:, 0, 1]
    array([0, 1])

This is the coordinate grid *implied by* a shape of (5, 4).

Now imagine I wanted to do a transformation on these coordinates. Say I wanted
to add 2 to the first (i) coordinate:

.. nbplot::

    >>> coordinate_grid[0, :, :] += 2

Now my coordinate grid expresses a *mapping* between a given (:math:`i, j`)
coordinate, and the new coordinate (:math:`i', j'`. I look up the new
coordinate using the :math:`i, j` index into the coordinate grid:

.. nbplot::

    >>> coordinate_grid[:, 0, 0]  # look up new coordinate for (0, 0)
    array([2, 0])
    >>> coordinate_grid[:, 1, 0]  # look up new coordinate for (1, 0)
    array([3, 0])
    >>> coordinate_grid[:, 0, 1]  # look up new coordinate for (0, 1)
    array([2, 1])

This means we can use these coordinate grids as a *mapping* from an input set
of coordinates to an output set of coordinates, for each pixel / voxel.

As you can imagine, meshgrid extends to three dimensions or more:

.. nbplot::

    >>> output_shape = (5, 6, 7)
    >>> I, J, K = output_shape
    >>> i_coords, j_coords, k_coords = np.meshgrid(range(I),
    ...                                            range(J),
    ...                                            range(K),
    ...                                            indexing='ij')
    >>> coordinate_grid = np.array([i_coords, j_coords, k_coords])
    >>> coordinate_grid.shape
    (3, 5, 6, 7)

.. nbplot::

    >>> coordinate_grid[:, 0, 0, 0]
    array([0, 0, 0])
    >>> coordinate_grid[:, 1, 0, 0]
    array([1, 0, 0])
    >>> coordinate_grid[:, 0, 1, 0]
    array([0, 1, 0])
    >>> coordinate_grid[:, 0, 0, 1]
    array([0, 0, 1])
