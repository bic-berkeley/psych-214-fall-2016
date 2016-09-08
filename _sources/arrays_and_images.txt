##################################
Arrays as images, images as arrays
##################################

You can consider arrays as images, and images as arrays.

We start off with our usual imports:

.. nbplot::

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt

Let's make an array of numbers between 0 through 99:

.. nbplot::

    >>> an_array = np.array([[ 0,  0,  0,  0,  0,  0,  0,  0],
    ...                      [ 0,  0,  0,  9, 99, 99, 94,  0],
    ...                      [ 0,  0,  0, 25, 99, 99, 79,  0],
    ...                      [ 0,  0,  0,  0,  0,  0,  0,  0],
    ...                      [ 0,  0,  0, 56, 99, 99, 49,  0],
    ...                      [ 0,  0,  0, 73, 99, 99, 31,  0],
    ...                      [ 0,  0,  0, 91, 99, 99, 13,  0],
    ...                      [ 0,  0,  9, 99, 99, 94,  0,  0],
    ...                      [ 0,  0, 27, 99, 99, 77,  0,  0],
    ...                      [ 0,  0, 45, 99, 99, 59,  0,  0],
    ...                      [ 0,  0, 63, 99, 99, 42,  0,  0],
    ...                      [ 0,  0, 80, 99, 99, 24,  0,  0],
    ...                      [ 0,  1, 96, 99, 99,  6,  0,  0],
    ...                      [ 0, 16, 99, 99, 88,  0,  0,  0],
    ...                      [ 0,  0,  0,  0,  0,  0,  0,  0]])
    >>> an_array.shape
    (15, 8)

In fact this array represents a monochrome picture of a letter.

We can show arrays as images using the ``plt.imshow`` command from
matplotlib_. Here is the default output:

.. nbplot::

    >>> plt.imshow(an_array)
    <...>

If you have a version of matplotlib older than version 2.0, this image will
look rather blurry. This is because matplotlib is drawing an image with many
more pixels than the array has values. For the pixels in-between array values,
older matplotlib has a default of using `linear interpolation`_ to estimate a
good pixel value. We can turn off this blurring effect by using `nearest
neighbor interpolation`_ instead of linear interpolation:

.. nbplot::

    >>> plt.imshow(an_array, interpolation='nearest')
    <...>

``nearest`` interpolation is the default value for matplotlib 2.0 and later.
If you have an older matplotllib and you'd like ``nearest`` interpolation to
be the default for the current session, use:

.. nbplot::

    >>> # Set nearest neighbor interpolation by default
    >>> plt.rcParams['image.interpolation'] = 'nearest'

The image is weirdly colorful. That is because matplotlib is using the default
*colormap*. A colormap is a mapping from values in the array to colors. In
matplotlib < 2.0 the default colormap is called ``jet`` and maps low numbers
in the image (0 in our case) to blue, and high numbers (99 in our case) to
red. For matplotlib version 2.0 and above the default colormap is called
``viridis``.  ``viridis`` maps low numbers to purple and high numbers to
yellow.

We can see the relationship of the numbers to the colors by asking matplotlib
to show the colormap:

.. nbplot::

    >>> # Nearest interpolation is now the default
    >>> plt.imshow(an_array)
    <...>
    >>> plt.colorbar()
    <...>

In our case, our image would make more sense as grayscale, so we use the
``gray`` colormap, like this:

.. nbplot::

    >>> plt.imshow(an_array, cmap='gray')
    <...>
    >>> plt.colorbar()
    <...>

A grayscale image is an array containing numbers giving the pixel intensity
values - in our case between 0 and 99.

Here we set ``gray`` to the default colormap for the rest of our plots:

.. nbplot::

    >>> # Set 'gray' as the default colormap
    >>> plt.rcParams['image.cmap'] = 'gray'

We can also plot lines in matplotlib. For example, we might want to plot the
values in row 8 from this array.  Because Python indices start at 0, this is
the 9th row of the array.

.. nbplot::

    >>> plt.plot(an_array[8])
    [...]

The x axis is the position in the array (0 through 7) and the y axis is the
value of the array row at that position.

The plot shows us the 0 values at the edges of the bar of the "i", an the ramp
up to the peak at the middle of the bar of the "i", in columns number 3 and 4.

A transpose in numpy uses the ``.T`` method on the array. This has the effect
of flipping the rows and columns (in 2D):

.. nbplot::

    >>> an_array.T
    array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1, 16,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  9, 27, 45, 63, 80, 96, 99,  0],
           [ 0,  9, 25,  0, 56, 73, 91, 99, 99, 99, 99, 99, 99, 99,  0],
           [ 0, 99, 99,  0, 99, 99, 99, 99, 99, 99, 99, 99, 99, 88,  0],
           [ 0, 99, 99,  0, 99, 99, 99, 94, 77, 59, 42, 24,  6,  0,  0],
           [ 0, 94, 79,  0, 49, 31, 13,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]])

.. nbplot::

    >>> # Defaults of nearest interpolation and gray colormap
    >>> plt.imshow(an_array.T)
    <...>

We can also reshape the original array to a 1D array, by stacking all the rows
end to end:

.. nbplot::

    >>> old_shape = an_array.shape
    >>> a_1d_array = np.reshape(an_array, old_shape[0] * old_shape[1])
    >>> a_1d_array
    array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 99, 99, 94,  0,  0,
            0,  0, 25, 99, 99, 79,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0, 56, 99, 99, 49,  0,  0,  0,  0, 73, 99, 99, 31,  0,  0,  0,  0,
           91, 99, 99, 13,  0,  0,  0,  9, 99, 99, 94,  0,  0,  0,  0, 27, 99,
           99, 77,  0,  0,  0,  0, 45, 99, 99, 59,  0,  0,  0,  0, 63, 99, 99,
           42,  0,  0,  0,  0, 80, 99, 99, 24,  0,  0,  0,  1, 96, 99, 99,  6,
            0,  0,  0, 16, 99, 99, 88,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0])

.. nbplot::

    >>> a_1d_array.shape
    (120,)

Reshaping the array to one dimension is a common operation, so there is a
separate numpy command for that, ``np.ravel``:

.. nbplot::

    >>> np.ravel(an_array)
    array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 99, 99, 94,  0,  0,
            0,  0, 25, 99, 99, 79,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0, 56, 99, 99, 49,  0,  0,  0,  0, 73, 99, 99, 31,  0,  0,  0,  0,
           91, 99, 99, 13,  0,  0,  0,  9, 99, 99, 94,  0,  0,  0,  0, 27, 99,
           99, 77,  0,  0,  0,  0, 45, 99, 99, 59,  0,  0,  0,  0, 63, 99, 99,
           42,  0,  0,  0,  0, 80, 99, 99, 24,  0,  0,  0,  1, 96, 99, 99,  6,
            0,  0,  0, 16, 99, 99, 88,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0])

One use of the 1D version of the array, is for making a histogram of the
distribution of values in the array:

.. nbplot::

    >>> plt.hist(a_1d_array)
    (...)

By default, the ``plt.hist`` function uses 50 bins, but you can specify how
many bins you want with the ``bins`` keyword:

.. nbplot::

    >>> plt.hist(a_1d_array, bins=75)
    (...)

As you can imagine, it's not hard to go back to the 2D shape, by splitting the
1D array back into 15 rows of 8 values each (and therefore 8 columns):

.. nbplot::

    >>> array_back = np.reshape(a_1d_array, (15, 8))
    >>> array_back
    array([[ 0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  9, 99, 99, 94,  0],
           [ 0,  0,  0, 25, 99, 99, 79,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0, 56, 99, 99, 49,  0],
           [ 0,  0,  0, 73, 99, 99, 31,  0],
           [ 0,  0,  0, 91, 99, 99, 13,  0],
           [ 0,  0,  9, 99, 99, 94,  0,  0],
           [ 0,  0, 27, 99, 99, 77,  0,  0],
           [ 0,  0, 45, 99, 99, 59,  0,  0],
           [ 0,  0, 63, 99, 99, 42,  0,  0],
           [ 0,  0, 80, 99, 99, 24,  0,  0],
           [ 0,  1, 96, 99, 99,  6,  0,  0],
           [ 0, 16, 99, 99, 88,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0]])
    >>> plt.imshow(array_back)
    <...>

In numpy, basic operations like multiplication, addition, comparison, are
always elementwise. For example, this multiplies every array value by 10:

.. nbplot::

    >>> an_array * 10
    array([[  0,   0,   0,   0,   0,   0,   0,   0],
           [  0,   0,   0,  90, 990, 990, 940,   0],
           [  0,   0,   0, 250, 990, 990, 790,   0],
           [  0,   0,   0,   0,   0,   0,   0,   0],
           [  0,   0,   0, 560, 990, 990, 490,   0],
           [  0,   0,   0, 730, 990, 990, 310,   0],
           [  0,   0,   0, 910, 990, 990, 130,   0],
           [  0,   0,  90, 990, 990, 940,   0,   0],
           [  0,   0, 270, 990, 990, 770,   0,   0],
           [  0,   0, 450, 990, 990, 590,   0,   0],
           [  0,   0, 630, 990, 990, 420,   0,   0],
           [  0,   0, 800, 990, 990, 240,   0,   0],
           [  0,  10, 960, 990, 990,  60,   0,   0],
           [  0, 160, 990, 990, 880,   0,   0,   0],
           [  0,   0,   0,   0,   0,   0,   0,   0]])

Comparison is also elementwise. For example, this gives True for every value >
50, and False for every value <= 50:

.. nbplot::

    >>> an_array > 50
    array([[False, False, False, False, False, False, False, False],
           [False, False, False, False,  True,  True,  True, False],
           [False, False, False, False,  True,  True,  True, False],
           [False, False, False, False, False, False, False, False],
           [False, False, False,  True,  True,  True, False, False],
           [False, False, False,  True,  True,  True, False, False],
           [False, False, False,  True,  True,  True, False, False],
           [False, False, False,  True,  True,  True, False, False],
           [False, False, False,  True,  True,  True, False, False],
           [False, False, False,  True,  True,  True, False, False],
           [False, False,  True,  True,  True, False, False, False],
           [False, False,  True,  True,  True, False, False, False],
           [False, False,  True,  True,  True, False, False, False],
           [False, False,  True,  True,  True, False, False, False],
           [False, False, False, False, False, False, False, False]], dtype=bool)

Matplotlib will treat False as 0 and True as 1, so this is one way of
binarizing the image at a threshold (of 50 in this case):

.. nbplot::

    >>> plt.imshow(an_array > 50)
    <...>

We can slice arrays as we slice strings or lists. The difference for arrays is
that we can slice in any or all dimensions at the same time.  For example, to
get the dot of the "i" it looks (from the numbers at the sides of the ploat)
that we want to the top 4 rows, and the last 5 columns:

.. nbplot::

    >>> an_array[0:4, 3:]
    array([[ 0,  0,  0,  0,  0],
           [ 9, 99, 99, 94,  0],
           [25, 99, 99, 79,  0],
           [ 0,  0,  0,  0,  0]])
    >>> plt.imshow(an_array[0:4, 3:])
    <...>
