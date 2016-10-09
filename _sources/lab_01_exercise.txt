###############
Lab 01 exercise
###############

* For code template see: :download:`lab_01_code.py`;
* For solution see: :doc:`lab_01_solution`.


.. testsetup::

    # Here I set up some useful things for the doctests below
    import numpy as np
    np.set_printoptions(precision=6)  # Only show 6 decimals when printing
    import matplotlib
    matplotlib.use('agg')  # Stop plots displaying on screen for tests

.. nbplot::
    :include-source: false

    >>> #: Compatibility with Python 2
    >>> from __future__ import print_function  # print('me') instead of print 'me'
    >>> from __future__ import division  # 1/2 == 0.5, not 0

*************
Simple arrays
*************

.. 5 minutes.

Create an array with variable name ``a`` and the following contents (shape (3,
4))::

   2  7 12  0
   3  9  3  4
   4  0  1  3

>>> #- create array "a" with values
>>> #-     2  7 12  0
>>> #-     3  9  3  4
>>> #-     4  0  1  3

What is the array ``shape``?

>>> #- Array shape?

What is the array ``ndim``?

>>> #- Array ndim?

How about the ``len`` of the array?

>>> #- Array length

Can you get the ``ndim`` and ``len`` from the shape?

>>> #- Get ndim and length from the shape

*******************************
Creating arrays using functions
*******************************

.. 10 minutes.

1. Create a 1D array from 2 through 5 inclusive.

>>> #- 1D array 2 through 5

2. Make an array with 10 equally spaced elements between 2 and 5 inclusive.

>>> #- 10 equally spaced elementd between 2 and 5

3. Make an all-ones array shape (4, 4).

>>> #- Shape 4,4 array of 1

4. Make an identity array shape (6, 6).

>>> #- Identity array shape 6, 6

5. Make this array with a single Python / numpy command::

    1  0  0
    0  2  0
    0  0  3

>>> #- Array with top left value == 1 etc

Look at the docstring for ``np.random.randn``.  Make a shape (3, 5) array with
random numbers from a standard normal distribution (a normal distribution with
mean 0 and variance 1).

>>> #- Array of random numbers shape 3, 5

*********************
Simple visualizations
*********************

.. 7 minutes.

1. Make an array ``x`` with 100 evenly spaced values between 0 and 2 * pi;

>>> #- x is an array with 100 evenly spaced numbers 0 - 2 pi

2. Make an array ``y`` which contains the cosine of the corresponding value in
   ``x`` - so ``y[i] = cos(x[i])`` (hint: ``np.lookfor('cosine')``).

>>> #- y has cosines of values in x

3. Plot ``x`` against ``y``;

>>> #- plot x against y

4. Make a 10 by 20 array of mean 0 variance 1 normal random numbers;

>>> #- Shape 10, 20 array of random numbers

5. Display this array as an image;

>>> #- Display as image

6. Investigate ``plt.cm``.  See if you can work out how to make the displayed
   image be grayscale instead of color.

>>> #- Grayscale image of array

************************************
Indexing and slicing, array creation
************************************

.. 10 minutes.

1. Create the following array, call this ``a`` (you did this before)::

    2  7 12  0
    3  9  3  4
    4  0  1  3

>>> #- Create array "a"

2. Get the 2nd row of ``a`` (``[ 3 9 3 4]``);

>>> #- 2nd row of a

3. Get the 3rd column of ``a`` (``[12 3 1]``);

>>> #- 3rd column of a

4. Create the following arrays (with correct data types)::

        [[1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 2],
         [1, 6, 1, 1]]

        [[0., 0., 0., 0., 0.],
         [2., 0., 0., 0., 0.],
         [0., 3., 0., 0., 0.],
         [0., 0., 4., 0., 0.],
         [0., 0., 0., 5., 0.],
         [0., 0., 0., 0., 6.]]

   Par on course: 3 statements for each

   *Hint*: Individual array elements can be accessed similarly to a list, e.g.
   ``a[1]`` or ``a[1, 2]``.

   *Hint*: Examine the docstring for ``diag``.

>>> #- Build given arrays


5. Skim through the documentation for ``np.tile``, and use this function to
   construct the array::

        [[4, 3, 4, 3, 4, 3],
         [2, 1, 2, 1, 2, 1],
         [4, 3, 4, 3, 4, 3],
         [2, 1, 2, 1, 2, 1]]

>>> #- Use np.tile to construct array

***********************************
Fancy indexing using boolean arrays
***********************************

.. 5 minutes.

1. Create the following array ``a`` (same as before)::

    2  7 12  0
    3  9  3  4
    4  0  1  3

>>> #- Create array a

2. Use ``>`` to make a mask that is true where the elements are greater than
   5, like this::

    False True  True  False
    False True  False False
    False False False False

>>> #- Make mask for values greater than 5

3. Return all the elements in ``a`` that are greater than 5.

>>> #- Return all values in a that are greater than 5

4. Set all the elements greater than 5 to be equal to 5, to get this::

    2  5  5  0
    3  5  3  4
    4  0  1  3

>>> #- Set all elements greater than 5 to equal 5

**********************
Elementwise operations
**********************

.. 10 minutes.

Remember our array ``a``::

   2  7 12  0
   3  9  3  4
   4  0  1  3

1. Use array slicing to get a new array composed of the even columns (0, 2) of
   ``a``. Now get array that contains the odd columns (1, 3) of ``a``.  Add
   these two arrays.

>>> #- Add even and odd columns of a

2. Generate this array::

    [2**0, 2**1, 2**2, 2**3, 2**4]

>>> #- Generate array of powers of 2

3. Generate an array length 10 such that this is true of the elements (where
   ``x[i]`` is the element of ``x`` at index ``i``)::

    x[i] = 2 ** (3 * i) - i

>>> #- Generate array

*****************
Summary functions
*****************

Remember our array ``a``::

   2  7 12  0
   3  9  3  4
   4  0  1  3


What are the:

* sum of all the values?

>>> #- Sum of values in a

* sum of the columns?

>>> #- Sum of the values of the columns in a

* sum of the rows?

>>> #- Sum of the values of the rows in a

* mean?

>>> #- Mean of all the values in a

* min?

>>> #- Minimum of all the values in a

* max?

>>> #- Maximum of all the values in a
