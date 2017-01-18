###################
List comprehensions
###################

List comprehensions are a nice short-cut for simple ``for`` loops in Python.

The list comprehension is a single expression that returns a list, element by
element.

Let's say you wanted to create a list of values for squared numbers. You might
do it like this:

.. nbplot::

    >>> squared_numbers = []
    >>> for i in range(10):  # numbers 0 through 9
    ...     squared_numbers.append(i ** 2)
    >>> squared_numbers
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

It turns out this kind of thing is a very common pattern in Python. The
pattern is: create an empty list, then use a for loop to fill in values for
the list.

List comprehensions are a short cut for that pattern:

.. nbplot::

    >>> squared_numbers = [i ** 2 for i in range(10)]
    >>> squared_numbers
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

The list comprehesion is an *expression*, starting and ending with square
brackets. The first thing inside the square brackets is the expression that
will become the element of the list - in this case ``i ** 2`` |--| followed by
a ``for`` clause - in this case ``for in in range(10)`` |--| that will feed
the first expression with values to use.

See the `Python docs on list comprehensions
<https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>`__
for more detail.

List comprehensions can be a little hard to read when you are not used to
them. If you find them confusing, as most of us do at first, then unpack them
into the equivalent ``for`` loop. Over time, as you get used to them, they can
be easier to read than the longer ``for`` loop equivalent.
