############################
Brisk introduction to Python
############################

This is an introduction designed for those of us who already know a `dynamic
programming language
<https://en.wikipedia.org/wiki/Dynamic_programming_language>`_ fairly well.
MATLAB and R are `examples of dynamic programming languages
<https://en.wikipedia.org/wiki/Dynamic_programming_language#Examples_of_Dynamic_Programming_Languages>`_.

.. testsetup::

    import os

.. nbplot::
    :include-source: false

    from __future__ import print_function, division

*******
Numbers
*******

There are two types of numbers in Python: integer and floating point.  In
Python, an integer is an *object* of type ``int``, and a float is an object of
type ``float``.

.. nbplot::

    >>> a = 99
    >>> type(a)
    <class 'int'>
    >>> b = 99.0
    >>> type(b)
    <class 'float'>

You can create ints and floats by using the ``int`` and ``float`` object
constructors:

.. nbplot::

    >>> float('1')
    1.0
    >>> float(1)
    1.0
    >>> int('1')
    1
    >>> int(1)
    1

``+``,  ``-``, ``*`` or ``/`` on a mix of floats and ints, give floats:

.. nbplot::

    >>> a + b
    198.0
    >>> a * b
    9801.0

Dividing an int by an int also gives a float |--| but this is only true by
default for Python >= 3 (see [#py2-division]_):

.. nbplot::

    >>> 1 / 2
    0.5

If you only want the integer result of the division, use ``//``

.. nbplot::

    >>> 1 // 2
    0

Python has built-in function called ``round``:

.. nbplot::

    >>> round(5 / 2)
    2

The ``%`` operator on numbers gives you the remainder of integer division
(also known as the modulus):

.. nbplot::

    >>> 5 % 2
    1

.. nbplot::

    >>> 5.0 % 2.0
    1.0

**************
True and False
**************

``True`` and ``False`` are special objects in Python.  They are of type
``bool`` (for Boolean).

.. nbplot::

    >>> type(True)
    <class 'bool'>

.. nbplot::

    >>> type(False)
    <class 'bool'>

.. nbplot::

    >>> True == False
    False
    >>> True == True
    True
    >>> False == False
    True

You can use the logical operators ``and``, ``or`` and ``not`` to express logic
about Boolean values:

.. nbplot::

    >>> True and True
    True
    >>> True and False
    False
    >>> True or False
    True
    >>> False or False
    False
    >>> not True
    False
    >>> True and not False
    True

****
None
****

``None`` is also a special object in Python.  By convention, Python often uses
``None`` to mean that no valid value resulted from an operation, or to signal
that we don't have a value for a parameter.

.. nbplot::

    >>> type(None)
    <class 'NoneType'>
    >>> None == None
    True

Unlike most other values in Python, the default display output from None, is
nothing:

.. nbplot::

    >>> None

******
Equals
******

As for MATLAB, ``=`` is for assignment, ``==`` is for testing equality.

.. nbplot::

    >>> a = 1
    >>> a
    1
    >>> a == 1
    True

Python uses ``!=`` for testing that objects are *not* equal. This is different
from e.g. MATLAB, which uses ``~=``:

.. nbplot::

    >>> a != 1
    False

*************************************
"If" statements, blocks and indention
*************************************

A conditional statement in Python looks like this:

.. nbplot::

    >>> my_var = 10
    >>> if my_var == 10:
    ...     print("The conditional is True!")
    ...     print("my_var does equal 10")
    ...
    The conditional is True!
    my_var does equal 10

The first line of the conditional statement, that contains the conditional
test, ends in a colon.  Call this the *if test*.  There follow some lines
*indented* relative to the ``if`` test.  Call these indented lines the *if
block*.  Python executes the statements in the ``if`` block only when the
``if`` test evaluates to True.

.. nbplot::

    >>> my_var = 11
    >>> # This time the conditional evaluates to False
    >>> if my_var == 10:  # the "if test"
    ...     # The indented lines are the "if block"
    ...     print("The conditional is True!")
    ...     print("my_var does equal 10")
    ...


The first line that returns to the same level of indentation as the ``if``
test line, closes the ``if`` block.

Unless the ``if`` block has a further indented block (for example, another
``if`` block), then all the lines in the block must have the same indentation.

The ``if`` block may be followed by another block where the conditional is
``else:``. This block will only run if the initial conditional test evaluates
to False.

.. nbplot::

    >>> my_var = 11
    >>> if my_var == 10:
    ...     print("The conditional is True!")
    ...     print("my_var does equal 10")
    ... else:
    ...     print("The conditional is False!")
    ...     print("my_var does not equal 10")
    ...
    The conditional is False!
    my_var does not equal 10

There may be other conditional tests, with associated conditional blocks.
These tests use the contraction ``elif conditional_test``, where ``elif`` is a
contraction for ``else if``:

.. nbplot::

    >>> my_var = 12
    >>> if my_var == 10:
    ...     print("The conditional is True!")
    ...     print("my_var does equal 10")
    ... elif my_var == 11:
    ...     print("The second conditional is True!")
    ...     print("my_var does equal 11")
    ... elif my_var == 12:
    ...     print("The third conditional is True!")
    ...     print("my_var does equal 12")
    ... else:
    ...     print("All conditionals are False!")
    ...     print("my_var does not equal 10, 11 or 12")
    ...
    The third conditional is True!
    my_var does equal 12

******************
"While" statements
******************

``while`` statements are another example with an initial test followed by an
indented block.   Here's an example where we find the largest `Fibonacci
number <https://en.wikipedia.org/wiki/Fibonacci_number>`_ less than 1000:

.. nbplot::

    >>> last_but_1 = 0
    >>> fibonacci = 1
    >>> while fibonacci < 1000:
    ...     last_but_2 = last_but_1
    ...     last_but_1 = fibonacci
    ...     fibonacci = last_but_2 + last_but_1
    ...
    >>> print("Largest Fibonacci < 1000 is", last_but_1)
    Largest Fibonacci < 1000 is 987

Notice the initial *while test*: ``while fibonacci < 1000:``, followed by the
indented *while block*.  Unlike the ``if`` statement, Python will continue to
run the statements in the ``while`` block until the conditional in the
``while`` test evaluates to False.

*****
Lists
*****

Make a list like this:

.. nbplot::

    >>> my_list = [9, 4, 7, 0, 8]
    >>> my_list
    [9, 4, 7, 0, 8]

.. nbplot::

    >>> type(my_list)
    <class 'list'>

A list element can be any type of object, including another list:

.. nbplot::

    >>> mixed_list = [9, 3.0, True, my_list]
    >>> mixed_list
    [9, 3.0, True, [9, 4, 7, 0, 8]]

.. nbplot::

    >>> type(mixed_list)
    <class 'list'>

Lists are sequences
===================

A sequence is type of Python object that has a defined element order, has a
length, is iterable, can be indexed with integers, and *sliced* (see below).
So, if object ``s`` is a sequence, then:

* ``s`` has a length that can be found with ``len(s)``;
* we can iterate over the elements in ``s`` with ``for element in s: # do
  something with element``;
* we can return the element at position ``n`` with ``s[n]``;
* we can get another sequence by *slicing* ``s``.  For example, ``s[0:n]``
  will give a new sequence containing the first ``n`` elements of ``s``.

.. nbplot::
    :include-source: false

    >>> # We check that our list is an instance of the type Sequence.
    >>> import collections
    >>> isinstance(my_list, collections.Sequence)
    True

.. nbplot::

    >>> # Has a length
    >>> len(my_list)
    5

.. nbplot::

    >>> # Is iterable
    >>> for e in my_list:
    ...     print(e)
    9
    4
    7
    0
    8

Notice that the ``for`` has the same form as the conditionals, with a first
line ending in a colon, followed by an indented block.

.. nbplot::

    >>> # Can be indexed
    >>> my_list[1]
    4
    >>> # Can be sliced
    >>> my_list[0:2]
    [9, 4]

Python indices are 0-based
==========================

Indices for Python sequences start at 0.  For Python, the first element is at
index 0, the second element is at index 1, and so on:

.. nbplot::

    >>> my_list[0]
    9
    >>> my_list[1]
    4

Negative indices
================

Negative numbers as indices count back from the end of the list. For
example, use index ``-1`` to return the last element in the list:

.. nbplot::

    >>> my_list
    [9, 4, 7, 0, 8]
    >>> my_list[-1]
    8

This is the third from last element:

.. nbplot::

    >>> my_list[-3]
    7

Lists are mutable
=================

A list is a *mutable* object. Mutable means, that we can change the elements
in the list, without creating a new list.

.. nbplot::

    >>> my_list[1] = 99
    >>> my_list
    [9, 99, 7, 0, 8]

In Python, variable names point to an object.

When you do ``another_variable = a_variable``, you are telling the name
``another_variable`` to point to the same object as the name
``a_variable``. When objects are mutable, this can be confusing:

.. nbplot::

    >>> another_list = my_list
    >>> another_list
    [9, 99, 7, 0, 8]

``my_list`` points to a list object in memory. When you do
``another_list = my_list``, it tells Python that ``another_list`` points
to *the same object*. So, if we modify the list, pointed to by
``my_list``, we also modify the value of ``another_list``, because ``my_list``
and ``another_list`` point at the same list.

.. nbplot::

    >>> my_list[1] = 101
    >>> another_list
    [9, 101, 7, 0, 8]

Adding lists
============

Adding two lists with ``+`` returns a new list that is the concatenation of
the two lists:

.. nbplot::

    >>> my_list + [False, 1, 2]
    [9, 101, 7, 0, 8, False, 1, 2]

Appending and removing elements
===============================

You can append elements with the ``append`` method.

A method is a function attached to the object.  See :ref:`functions` for more
on functions in Python.

We can see that ``append`` is a method by displaying the value of
``my_list.append``:

.. nbplot::

    >>> my_list.append
    <built-in method append of list object at 0x...>

To call the method, we add parentheses, surrounding any arguments we want to
pass into the method.  In this case we want to pass in the element to append:

.. nbplot::

    >>> my_list.append(20)
    >>> my_list
    [9, 101, 7, 0, 8, 20]

Note that the ``append`` method does *not* return the list, it just changes
the list in-place. Python returns ``None`` from the ``append`` method:

.. nbplot::

    >>> result = my_list.append(42)
    >>> result == None
    True

This is also true for some other methods that modify the list in-place, such
as the ``sort`` method:

.. nbplot::

    >>> new_list = [10, 1, 3]
    >>> result = new_list.sort()
    >>> # Return value is None
    >>> result == None
    True
    >>> # But the original list now in ascending order from sort
    >>> new_list
    [1, 3, 10]

You can remove elements from the list with the ``pop`` method:

.. nbplot::

    >>> # Remove and return the last element of the list
    >>> my_list.pop()
    42
    >>> my_list
    [9, 101, 7, 0, 8, 20]
    >>> # Remove and return the third element of the list
    >>> my_list.pop(2)
    7
    >>> my_list
    [9, 101, 0, 8, 20]

.. _slicing:

Slicing
=======

You can return slices from any sequence, including lists, by putting a slice
specifier in square brackets. For example, this returns the first 3 elements
of the list:

.. nbplot::

    >>> my_list[0:3]
    [9, 101, 0]

The first number after the square bracket and before the colon is the *start*
index. In this case we start at the first element (element at index 0). The
second number, after the colon, is the *stop* index. This is the end index
*plus one*.  So we return elements at index 0, 1 and 2. That is, elements *up
to, but not including* 3.

If you omit the first number (the start index) Python assumes 0:

.. nbplot::

    >>> my_list[:3]
    [9, 101, 0]

If you omit the second number, Python assumes the length of the list as
the stop index.

.. nbplot::

    >>> my_list[2:]
    [0, 8, 20]
    >>> my_list[2:len(my_list)]
    [0, 8, 20]

You can omit both numbers, in which case you return all the elements of the
list. This can be useful if you want to make another list that contains the
same elements as the first:

.. nbplot::

    >>> another_list = my_list[:]
    >>> another_list
    [9, 101, 0, 8, 20]

Because this is a new list object, you can change the original list without
changing the new list:

.. nbplot::

    >>> my_list[1] = 999
    >>> another_list
    [9, 101, 0, 8, 20]

You can also specify a second colon, and a third number. This third
number is the *step size*. For example, to get every second element of
the list:

.. nbplot::

    >>> my_list[0:4:2]
    [9, 0]

You can use negative numbers for the start and stop indices:

.. nbplot::

    >>> my_list
    [9, 999, 0, 8, 20]
    >>> my_list[-4:-2]
    [999, 0]

Negative numbers for the step have the obvious meaning:

.. nbplot::

    >>> my_list[4:1:-1]
    [20, 8, 0]

If you have a negative step size, and you don't specify the start index, then
the start index defaults to the last element in the list. If you don't specify
the stop index, it defaults to one below 0:

.. nbplot::

    >>> my_list
    [9, 999, 0, 8, 20]
    >>> my_list[-1:1:-1]
    [20, 8, 0]
    >>> my_list[:1:-1]
    [20, 8, 0]
    >>> my_list[-2::-1]
    [8, 0, 999, 9]

One consequence that is worth remembering is that the following idiom gives
you a reversed copy of the list:

.. nbplot::

    >>> my_list[::-1]
    [20, 8, 0, 999, 9]

******
Tuples
******

Tuples are almost the same as lists, except they are not mutable. That
is, you cannot change the elements of a tuple, or change the number of
elements.

.. nbplot::

    >>> my_tuple = (9, 4, 7, 0, 8)
    >>> my_tuple
    (9, 4, 7, 0, 8)

.. nbplot::

    >>> # This raises a TypeError
    >>> # my_tuple[1] = 99

.. nbplot::

    >>> # This raises an AttributeError, because tuples have no append method
    >>> # my_tuple.append(20)

Here's an empty tuple:

.. nbplot::

    >>> empty_tuple = ()
    >>> empty_tuple
    ()

A tuple with two elements:

.. nbplot::

    >>> two_tuple = (1, 5)
    >>> two_tuple
    (1, 5)

There is a little complication when making a tuple with one element:

.. nbplot::

    >>> not_a_tuple = (1)
    >>> not_a_tuple
    1

This is because Python can't tell that you meant this to be a tuple,
rather than an expression with parentheses round it:

.. nbplot::

    >>> not_a_tuple = (1 + 5 + 3)
    >>> not_a_tuple
    9

To tell Python that you mean this to be a length-one tuple, add a comma after
the element, and before the closing parenthesis:

.. nbplot::

    >>> one_tuple = (1,)
    >>> one_tuple
    (1,)

*******
Strings
*******

Make a string like this:

.. nbplot::

    >>> my_string = 'interesting text'
    >>> my_string
    'interesting text'

You can use single quotes or double quotes for your string, the two strings
are the same:

.. nbplot::

    >>> another_string = "interesting text"
    >>> another_string
    'interesting text'
    >>> my_string == another_string
    True

Convert other objects to strings using ``str``:

.. nbplot::

    >>> # Convert integer to string
    >>> str(9)
    '9'
    >>> # Convert floating point value to string
    >>> str(1.2)
    '1.2'

Strings are sequences
=====================

Like lists, strings are sequences (have length, can be iterated, can index,
can slice).

.. nbplot::

    >>> # Length
    >>> len(my_string)
    16

    >>> # Iterable
    >>> for c in my_string:
    ...     print(c)
    i
    n
    t
    e
    r
    e
    s
    t
    i
    n
    g
    <BLANKLINE>
    t
    e
    x
    t

    >>> # Can index
    >>> my_string[1]
    'n'

    >>> # Can slice
    >>> my_string[1:5]
    'nter'

Strings are immutable
=====================

Unlike lists, strings are immutable. You cannot change the characters within a
string:

.. nbplot::

    >>> # Raises a TypeError
    >>> # my_string[1] = 'N'

Adding strings
==============

.. nbplot::

    >>> my_string + ' with added insight'
    'interesting text with added insight'

String methods
==============

Strings have lots of interesting methods. In IPython, try tab-complete on a
string variable name, followed by a period |--| e.g. type ``my_string.``,
followed by the tab key.  See also the `list of string methods in the Python
docs <http://docs.python.org/library/stdtypes.html#string-methods>`_.

One interesting method is ``replace``. It returns a new string that is a copy
of the input, but replacing instances of one string with another:

.. nbplot::

    >>> another_string = my_string.replace('interesting', 'extraordinary')
    >>> another_string
    'extraordinary text'

Notice that the original string has not changed (it's immutable):

.. nbplot::

    >>> my_string
    'interesting text'

Use the ``split`` method to break a string into a list of strings.  By
default, ``split`` will split the string at any white space (spaces tab
characters or line breaks):

.. nbplot::

    >>> my_string.split()
    ['interesting', 'text']

Pass a character to ``split`` to split the string at that character:

.. nbplot::

    >>> another_example = 'one:two:three'
    >>> another_example.split(":")
    ['one', 'two', 'three']

The ``strip`` method returns a new string with spaces, tabs and end of line
characters removed from the beginning and end:

.. nbplot::

    >>> my_string = ' a string\n'
    >>> my_string
    ' a string\n'
    >>> my_string.strip()
    'a string'

Inserting values into strings
=============================

Use the ``format`` method to create new strings with inserted values:

.. nbplot::

    >>> shepherd = "Mary"
    >>> print("Shepherd {} is on duty.".format(shepherd))
    Shepherd Mary is on duty.

.. nbplot::

    >>> shepherd = "Mary"
    >>> age = 32
    >>> print("Shepherd {} is {} years old.".format(shepherd, age))
    Shepherd Mary is 32 years old.

You can do more complex formatting of numbers and strings using formatting
options within the curly brackets |--| see the `Python string format examples
<https://docs.python.org/3.5/library/string.html#format-examples>`_.

.. nbplot::

    >>> print("Number {:03d} is here.".format(11))
    Number 011 is here.

******
Ranges
******

``range`` in Python 3 returns a *range object*.  It is a sequence, and so it
is rather like a list [#py2-range]_:

.. nbplot::

    >>> my_range = range(5)
    >>> my_range
    range(0, 5)
    >>> len(my_range)
    5
    >>> for e in my_range:
    ...    print(e)
    0
    1
    2
    3
    4
    >>> my_range[1]
    1
    >>> my_range[0:2]
    range(0, 2)

You can make a range object into a list by using ``list``:

.. nbplot::

    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Set the start element for ``range`` by passing two arguments:

.. nbplot::

    >>> my_range = range(1, 7)
    >>> my_range
    range(1, 7)
    >>> list(my_range)
    [1, 2, 3, 4, 5, 6]

Set the step size with a third argument:

.. nbplot::

    >>> my_range = range(1, 7, 2)
    >>> my_range
    range(1, 7, 2)
    >>> list(my_range)
    [1, 3, 5]

****
Sets
****

Sets are collections of unique elements, with no defined order.  Python
reserves the right to order the elements in a set in any way it chooses:

.. nbplot::

    >>> # Only unique elements collected in the set
    >>> my_set = set((5, 3, 1, 3))
    >>> my_set  # doctest: +SKIP
    {1, 3, 5}

Because there is no defined order, you cannot index into a set:

.. nbplot::

    >>> # Raises a TypeError
    >>> # my_set[1]

You can add elements to a set with the ``add`` method:

.. nbplot::

    >>> my_set.add(10)
    >>> my_set  # doctest: +SKIP
    {1, 3, 5, 10}

Because set elements must be unique, if you add an element already in the set,
this does not change the set:

.. nbplot::

    >>> my_set.add(5)
    >>> my_set  # doctest: +SKIP
    {1, 3, 5, 10}

You can iterate over a set, but the order of the elements is arbitrary, and
you cannot rely on the same order in any two runs of your program:

.. nbplot::

    >>> for element in my_set:  # doctest: +SKIP
    ...     print(element)
    1
    3
    5

Look at the methods of the set object for interesting operations such as
``difference``, ``union``, ``intersection`` etc.

************
Dictionaries
************

A dictionary is an unordered collection of key |--| value pairs. The *key* is
something that identifies the element, and the *value* is the value
corresponding to the particular key.

.. nbplot::

    >>> # This is an empty dictionary
    >>> software = {}

Here we insert a new key |--| value mapping into the dictionary. The key is a
string |--| ``MATLAB``, and the corresponding value is an integer 50:

.. nbplot::

    >>> software['MATLAB'] = 50
    >>> software
    {'MATLAB': 50}

We can insert another key |--| value mapping:

.. nbplot::

    >>> software['Python'] = 100
    >>> software  #doctest: +SKIP
    {'Python': 100, 'MATLAB': 50}

We can get the value corresponding to a key by indexing the dictionary
with the key:

.. nbplot::

    >>> software['Python']
    100

We can iterate over the keys in the dictionary, but the order of the
keys is arbitrary. Python returns the keys in any order it chooses, and
we can't rely on the order being the same in any two runs of our
program:

.. nbplot::

    >>> for key in software.keys():  #doctest: +SKIP
    ...     print(key)
    MATLAB
    Python

We can also iterate over the values, with the same constraint, that the
order is arbitrary:

.. nbplot::

    >>> for value in software.values():  #doctest: +SKIP
    ...     print(value)

    50
    100

We can use the ``items`` method to iterate over the key |--| value pairs. In
this case each element is a tuple of length two, where the first element is
the key and the second element is the value:

.. nbplot::

    >>> for key_value in software.items():  #doctest: +SKIP
    ...     print(key_value)
    ('MATLAB', 50)
    ('Python', 100)

You can construct a dictionary with curly brackets, commas between the key
|--| value pairs, and colons separating the key and value:

.. nbplot::

    >>> software = {'MATLAB': 50, 'Python': 100}
    >>> software.items()  #doctest: +SKIP
    dict_items([('MATLAB', 50), ('Python', 100)])

Keys must be unique. A later key |--| value pair will overwrite an earlier key
|--| value pair that had the same key:

.. nbplot::

    >>> software = {'MATLAB': 50, 'Python': 100, 'MATLAB': 45}
    >>> software.items()  # doctest: +SKIP
    dict_items([('MATLAB', 45), ('Python', 100)])

**************************************
"for", "while", "continue" and "break"
**************************************

``for`` statements and ``while`` statement are *loops*, because Python 
keeps executing the ``for`` or ``while`` block until the ``for`` runs out of
elements or the ``while`` condition is False.  You can break out of a loop
using the ``break`` statement:

.. nbplot::

    >>> for i in range(10):
    ...     if i == 6:
    ...         break
    ...     print(i)
    ...
    0
    1
    2
    3
    4
    5

The ``continue`` statement short-circuits execution of the current iteration
of the ``for`` or ``while`` block, to continue with the next:

.. nbplot::

    >>> for i in range(10):
    ...     if i == 6:
    ...         continue
    ...     print(i)
    0
    1
    2
    3
    4
    5
    7
    8
    9

See :doc:`on_loops` for more on loops and ``break``.

.. _functions:

*********
Functions
*********

Here we define our first function in Python:

.. nbplot::

    >>> def my_function(an_argument):
    ...     return an_argument + 1

The function definition begins with the ``def`` keyword followed by a space.
There follows the name of the function ``my_function``. Next we have an open
parenthesis, followed by a specification of the arguments that the function
expects to be passed to it. In this case, the function expects a single
argument. In our case, the value of the input argument will be attached to the
name ``an_argument`` when the function starts to execute.  Last, we have an
indented block, with code that will run when the function is called. We can
return a value from the function using the ``return`` statement.

.. nbplot::

    >>> my_function(10)
    11

We called ``my_function`` by appending the opening parenthesis, and the
arguments, followed by the closing parenthesis. The function began to execute
with the variable ``an_argument`` set to 10. It returned 10 + 1 = 11.

A function need not accept any arguments:

.. nbplot::

    >>> def my_second_function():
    ...     return 42
    ...
    >>> my_second_function()
    42

A function does not need to have a ``return`` statement.  If there is no
return statement, the function returns ``None``:

.. nbplot::

    >>> def function_with_no_return():
    ...     # Function with no return statement
    ...     a = 1
    ...
    >>> function_with_no_return() == None
    True

A function can have more than one argument:

.. nbplot::

    >>> def my_third_function(first_argument, second_argument):
    ...     return first_argument + second_argument
    ...
    >>> my_third_function(10, 42)
    52

It is also possible to give a default value for a function argument:

.. nbplot::

    >>> def my_fourth_function(first_argument, extra_argument=101):
    ...     return first_argument + extra_argument

This function, like ``my_third_function``, has two arguments, and we can call
it the same way that we call ``my_third_function``:

.. nbplot::

    >>> my_fourth_function(10, 42)
    52

But, we can also omit the second argument, in which case it will get its
default value:

.. nbplot::

    >>> my_fourth_function(10)  # Pass one argument, get default for second
    111

So far we have passed in arguments by position, the first argument in our call
becoming the first argument in the function, and so on.  We can also pass in
arguments by name.  For example, we could pass in ``extra_argument`` by giving
the parameter name and value, like this:

.. nbplot::

    >>> my_fourth_function(10, extra_argument=202)
    212

Passing arguments this way can make the code easier to read, because it the
name of the argument often gives a good clue as to its purpose in the
function.  It can also be useful with functions having many parameters with
default values; in that case using the argument name makes it easier to pass
in one or few values that are different from the defaults.

Remember that everything in Python is an object. The function is itself an
object, where the name of the function is a variable, that refers to the
function:

.. nbplot::

    >>> my_fourth_function
    <function my_fourth_function at 0x...>

.. nbplot::

    >>> type(my_fourth_function)
    <class 'function'>

We call the function by adding the open parenthesis followed by the arguments
and the close parenthesis:

.. nbplot::

    >>> my_fourth_function(10)
    111

We can make a new name to point to this same function as easily as we can
could with any other Python variable:

.. nbplot::

    >>> another_reference_to_func4 = my_fourth_function
    >>> type(another_reference_to_func4)
    <class 'function'>
    >>> # We call this function using the new name
    >>> another_reference_to_func4(10)
    111

*******
Sorting
*******

The Python function ``sorted`` returns a sorted list from something that
Python can iterate over:

.. nbplot::

    >>> sorted('adcea')
    ['a', 'a', 'c', 'd', 'e']

.. nbplot::

    >>> sorted((1, 5, 3, 2))
    [1, 2, 3, 5]

In order to do the sorting, Python compares the elements with
``one_element < another_element``. For example, to do the sort above,
Python needed results like:

.. nbplot::

    >>> 3 < 5
    True

Sometimes you want to order the objects in some other way than simply
comparing the elements. If so, then you can define a *sort function*, that,
when given an element, returns a *sort value* for that element. Python does
the sorting, not on the elements themselves, but on the returned sort value
for each element.

For example, let's say we have first and last names stored as tuples:

.. nbplot::

    >>> people = [('JB', 'Poline'), ('Matthew', 'Brett'), ('Mark', 'DEsposito')]

By default, Python compares tuples by comparing the first value first, then
the second value, and so on. This means for our case that we are sorting on
the first name:

.. nbplot::

    >>> ('Matthew', 'Brett') > ('Mark', 'DEsposito')
    True

.. nbplot::

    >>> sorted(people)
    [('JB', 'Poline'), ('Mark', 'DEsposito'), ('Matthew', 'Brett')]

That may not be what you want.  You might want to sort by the last name, which
is the second value in the tuple.  In that case you can make a sort function,
that accepts the element as an input (the tuple in this case), and returns a
value:

.. nbplot::

    >>> def get_last_name(person):
    ...     return person[1]  # The last name

Remember everything in Python is an object. The function we have just defined
is also an object, with name ``get_last_name``:

.. nbplot::

    >>> get_last_name
    <function get_last_name at 0x...>

We can pass this value to the ``sorted`` function as a sort function.  We will
pass this in using the sort function parameter name, which is ``key``:

.. nbplot::

    >>> sorted(people, key=get_last_name)
    [('Matthew', 'Brett'), ('Mark', 'DEsposito'), ('JB', 'Poline')]

*****
Files
*****

You can open a file in several different *modes*.  The mode specifies whether
you want to read or write the file, and whether the data in the file is, or
will be, text string or binary data (bytes).  For example, here we open a file
for writing (``w``) text (``t``):

.. nbplot::

    >>> my_file = open("a_text_file.txt", "wt")

If we had wanted to write binary (byte) data, we would have used ``wb`` for
the mode (Write Binary).

As usual, you can explore this new file object in IPython by appending the
object name with a period, and pressing the tab key to get a list of
attributes and methods.

To write to a file use the ``write`` method.

.. nbplot::

    >>> # Write a line of text with a newline character at the end
    >>> # The method returns the number of characters written
    >>> my_file.write("MATLAB is good for matrices\n")
    28
    >>> # Another line
    >>> my_file.write("Python is good for coding\n")
    26

You should close the file when you've finished with it:

.. nbplot::

    >>> my_file.close()

To read a file, open the file in read mode:

.. nbplot::

    >>> # Open file in Read Text mode
    >>> my_file2 = open("a_text_file.txt", "rt")

You can read all the contents in one shot by calling the ``read`` method
without arguments:

.. nbplot::

    >>> contents = my_file2.read()
    >>> print(contents)
    MATLAB is good for matrices
    Python is good for coding
    <BLANKLINE>

Remember to close the file afterwards:

.. nbplot::

    >>> my_file2.close()

An open text file object is also *iterable*, meaning, that you can ask the
file object to return its contents line by line, in a ``for`` loop. Let's open
the file again to show this in action:

.. nbplot::

    >>> my_file2 = open("a_text_file.txt", "rt")
    >>> for line in my_file2:  # iterating over the file object
    ...     print("Line is:", line)
    ...
    Line is: MATLAB is good for matrices
    <BLANKLINE>
    Line is: Python is good for coding
    <BLANKLINE>
    >>> my_file2.close()

.. testcleanup::

    os.unlink('a_text_file.txt')

.. rubric:: Footnotes

.. [#py2-division] Python 3 returns a floating point value from dividing two
   integers, but the default for Python 2 is to return the integer part of the
   division.  Thus, in Python 2, ``1 / 2 == 1 // 2 == 0``. If your code may
   run on Python 2, remember to add the statement ``from __future__ import
   division`` at the top of your code files, to make sure you get the Python 3
   behavior when dividing integers.

.. [#py2-range] In Python 2, ``range`` returns a list.  You can often use a
   Python 3 range object in the same way you could use a list, so this often
   doesn't matter for the person using the code, but it is a difference you
   might have to take into account when writing code that runs on Python 2 as
   well as Python 3.
