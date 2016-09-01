############################
Brisk introduction to Python
############################

This is an introduction designed for those of us who already know a dynamic
programming language fairly well, such as MATLAB.

A first point that you will see recur throughout is: everything in Python is
an object

*******
Numbers
*******

There are two types of number in Python, integers, and floating point.
In Python, an integer is an *object* of type ``int``, and a float is an
object of type ``float``.

.. nbplot::

    >>> a = 99
    >>> type(a)
    <class 'int'>

.. nbplot::

    >>> b = 99.0
    >>> type(b)
    <class 'float'>

You can create ints and floats by using the ``int`` and ``float`` object
constructors:

.. nbplot::

    >>> float('1')
    1.0

.. nbplot::

    >>> float(1)
    1.0

.. nbplot::

    >>> int('1')
    1

.. nbplot::

    >>> int(1)
    1

``+ - * /`` on a mix of floats and ints, give floats

.. nbplot::

    >>> a + b
    198.0

.. nbplot::

    >>> a * b
    9801.0

Dividing an int by an int also gives a float |--| but this is only true by
default for Python >= 3:

.. nbplot::

    >>> 1 / 2
    0.5

If your code may run on Python 2, and you want division to return a float,
force one of the arguments to be a float:

.. nbplot::

    >>> 1 / float(2)
    0.5

If you only want the integer result of the division, use ``//``

.. nbplot::

    >>> 1 // 2
    0

Python has built-in function called ``round``:

.. nbplot::

    >>> round(5 / 2)
    2

The ``%`` operator on numbers gives you the remainder:

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

Python uses ``!=`` for testing that objects are not equal. This is different
from e.g. MATLAB, which uses ``~=``:

.. nbplot::

    >>> a != 1
    False

****************
If and indention
****************

A conditional block in Python looks like this:

.. nbplot::

    >>> my_var = 10
    >>> if my_var == 10:
    ...     print("The conditional is True!")
    ...     print("my_var does equal 10")
    The conditional is True!
    my_var does equal 10
    >>> print("Finished the conditional block")
    Finished the conditional block

Note that the first line of the conditional, that contains the conditional
test, ends in a colon.  All subsequent lines indented relative to that line
are executed only if the conditional is True.

The first line that returns to the same level of indentation as the initial
conditional statement, closes the block.  Call the first line: the
*conditional test* and the subsequent lines of indented statements: the
*conditional block*.

Unless the conditional block contains some other type of block (e.g. a ``for``
block or a ``while`` block), then all the lines in the block must have the
same indentation.

.. nbplot::

    >>> my_var = 11
    >>> if my_var == 10:
    ...     print("The conditional is True!")
    ...     print("my_var does equal 10")
    >>> print("Finished the conditional block")
    Finished the conditional block

There may also be a further block where the conditional is ``else``, which is
only run if the conditional test evaluates to False:

.. nbplot::

    >>> my_var = 11
    >>> if my_var == 10:
    ...     print("The conditional is True!")
    ...     print("my_var does equal 10")
    ... else:
    ...     print("The conditional is False!")
    ...     print("my_var does not equal 10")
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
    The third conditional is True!
    my_var does equal 12

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

Lists are *sequences*. A sequence is type of Python object that has a
defined element order, that has a length, is iterable, and can be
indexed with integers, and sliced with slice definitions. So, if object
``s`` is a sequence, then:

-  ``s`` has a length that can be found with ``len(s)``;
-  we can iterate over the elements in ``s`` with
   ``for element in s: # do something with element``;
-  we can return the element at position ``n`` with ``s[n]``;
-  we can get another sequence by *slicing* ``s`` - e.g. ``s[0:n]`` will
   give a new sequence containing the first ``n`` elements of ``s``.

.. nbplot::

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

.. nbplot::

    >>> # Can be sliced
    >>> my_list[0:2]
    [9, 4]

Notice that Python indices are 0-based. That means that the first
element is at index 0, the second element is at index 1, and so on:

.. nbplot::

    >>> my_list[0]
    9

Negative numbers as indices count back from the end of the list. For
example, use index ``-1`` to return the last element in the list:

.. nbplot::

    >>> my_list
    [9, 4, 7, 0, 8]

.. nbplot::

    >>> my_list[-1]
    8

This is the third from last element:

.. nbplot::

    >>> my_list[-3]
    7

A list is also *mutable*. Mutable means, that we can change the elements
in the list, without creating a new list.

.. nbplot::

    >>> isinstance(my_list, collections.MutableSequence)
    True

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
``my_list``, we also modify the contents of ``another_list``, because
``my_list`` and ``another_list`` point at the same list.

.. nbplot::

    >>> my_list[1] = 101
    >>> another_list
    [9, 101, 7, 0, 8]

An interesting thing you can do to list is add:

.. nbplot::

    >>> my_list + [False, 1, 2]
    [9, 101, 7, 0, 8, False, 1, 2]

You can append elements with the ``append`` method:

.. nbplot::

    >>> my_list.append(20)
    >>> my_list
    [9, 101, 7, 0, 8, 20]

Note that the ``append`` method does *not* return the list, it just
changes the list in-place. Python returns None from the ``append``
method:

.. nbplot::

    >>> result = my_list.append(42)
    >>> result == None
    True

You can delete elements with ``del``:

.. nbplot::

    >>> del my_list[2]
    >>> my_list
    [9, 101, 0, 8, 20, 42]

You can return slices from any sequence, including lists, by putting a
slice specifier in square brackets. For example, this returns the first
3 elements of the list:

.. nbplot::

    >>> my_list[0:3]
    [9, 101, 0]

The first number before the colon is the *start* index, in this case
starting the first element (element at index 0). The second number,
after the colon, is the *stop* index. This is the end index *plus one*.
So we return elements at index 0, 1 and 2. That is, elements *up to, but
not including* 3.

If you omit the first number (the start index) Python assumes 0:

.. nbplot::

    >>> my_list[:3]
    [9, 101, 0]

If you omit the second number, Python assumes the length of the list as
the stop index.

.. nbplot::

    >>> my_list[2:]
    [0, 8, 20, 42]

.. nbplot::

    >>> my_list[2:len(my_list)]
    [0, 8, 20, 42]

You can omit both numbers, in which case you return all the elements of
the list. This can be useful if you want to make another list that has
the elements as the first:

.. nbplot::

    >>> another_list = my_list[:]
    >>> another_list
    [9, 101, 0, 8, 20, 42]

Because this is a new list object, you can change the original list
without changing the new list:

.. nbplot::

    >>> my_list[1] = 999
    >>> another_list
    [9, 101, 0, 8, 20, 42]

You can also specify a second colon, and a third number. This third
number is the *step size*. For example, to get every second element of
the list:

.. nbplot::

    >>> my_list[0:4:2]
    [9, 0]

You can use negative numbers for the start and stop indices:

.. nbplot::

    >>> my_list[-4:-2]
    [0, 8]

Negative numbers for the step have the obvious meaning:

.. nbplot::

    >>> my_list[4:1:-1]
    [20, 8, 0]

If you have a negative step size, and you don't specify the start index,
then the start index defaults to the last element in the list. If you
don't specify the stop index, it defaults to one below 0:

.. nbplot::

    >>> my_list
    [9, 999, 0, 8, 20, 42]

.. nbplot::

    >>> my_list[-1:1:-1]
    [42, 20, 8, 0]

.. nbplot::

    >>> my_list[:1:-1]
    [42, 20, 8, 0]

.. nbplot::

    >>> my_list[-2::-1]
    [20, 8, 0, 999, 9]

One consequence that is worth remembering is that this idiom gives you a
reversed copy of the list:

.. nbplot::

    >>> my_list[::-1]
    [42, 20, 8, 0, 999, 9]

******
Tuples
******

Tuples are almost the same as lists, except they are not mutable. That
is, you cannot change the elements of a tuple, or add or remove
elements.

.. nbplot::

    >>> my_tuple = (9, 4, 7, 0, 8)
    >>> my_tuple
    (9, 4, 7, 0, 8)

.. nbplot::

    >>> isinstance(my_tuple, collections.Sequence)
    True

.. nbplot::

    >>> isinstance(my_tuple, collections.MutableSequence)
    False

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

There's a little complication in Python, when making a tuple with one
element:

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

To tell Python that you mean this to be a length-one tuple, add a comma
after the element, and before the closing parenthesis:

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

You can use single quotes or double quotes for your string, the two
strings are the same:

.. nbplot::

    >>> another_string = "interesting text"
    >>> another_string
    'interesting text'

.. nbplot::

    >>> my_string == another_string
    True

Like lists, strings are sequences (have length, can be iterated, can index,
can slice).

.. nbplot::

    >>> len(my_string)
    16

.. nbplot::

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

.. nbplot::

    >>> my_string[1]
    'n'

.. nbplot::

    >>> my_string[1:5]
    'nter'

Unlike lists, strings are immutable. You cannot change the characters
within a string:

.. nbplot::

    >>> # Raises a TypeError
    >>> # my_string[1] = 'N'

Strings have lots of interesting methods. Try tab-completing on a string
variable name, followed by a period - e.g. ``my_string.``.

One interesting method is ``replace``. It returns a new string,
replacing instances of one string with another:

.. nbplot::

    >>> another_string = my_string.replace('interesting', 'extraordinary')
    >>> another_string
    'extraordinary text'

Notice that the original string has not changed (it's immutable):

.. nbplot::

    >>> my_string
    'interesting text'

You can add strings:

.. nbplot::

    >>> my_string + ' with added insight'
    'interesting text with added insight'

****
Sets
****

Sets are collections of unique elements, with no defined order (Python
reserves the right to order sets in any way it chooses:

.. nbplot::

    >>> # Only unique elements collected in the set
    >>> my_set = set((5, 3, 1, 3))
    >>> my_set
    {1, 3, 5}

Because there is no defined order, you cannot index into a set:

.. nbplot::

    >>> # Raises a TypeError
    >>> # my_set[1]

You can iterate over a set, but order of the elements is arbitrary, and
you cannot rely on the same order in any two runs of your program:

.. nbplot::

    >>> for element in my_set:
    ...     print(element)
    1
    3
    5

Look at the methods of the set object for interesting operations such as
``difference``, ``union``, ``intersection`` etc.

************
Dictionaries
************

A dictionary is an unordered collection of key, value pairs. The *key*
is something that identifies the element, and the *value* is the value
corresponding a particular key.

.. nbplot::

    >>> # This is an empty dictionary
    >>> software = {}

.. nbplot::

    >>> # Show the keys
    >>> software.keys()
    dict_keys([])

.. nbplot::

    >>> # Show the values
    >>> software.values()
    dict_values([])

Here we make a new key value mapping. The key is a string - ``Python``,
and the corresponding value is an integer 100:

.. nbplot::

    >>> software['MATLAB'] = 50
    >>> software.keys()
    dict_keys(['MATLAB'])

Another key, value mapping:

.. nbplot::

    >>> software['Python'] = 100
    >>> software.keys()  #doctest: +SKIP
    dict_keys(['MATLAB', 'Python'])

.. nbplot::

    >>> software.values()  #doctest: +SKIP
    dict_values([50, 100])

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

We can use the ``items`` method to iterate over the key, value pairs. In
this case each element is a tuple of length two, where the first element
is the key and the second element is the value:

.. nbplot::

    >>> for key_value in software.items():  #doctest: +SKIP
    ...     print(key_value)

    ('MATLAB', 50)
    ('Python', 100)

You can construct a dictionary with curly brackets, commas between the
key, value pairs, and colons separating the key and value:

.. nbplot::

    >>> software = {'MATLAB': 50, 'Python': 100}
    >>> software.items()  #doctest: +SKIP
    dict_items([('MATLAB', 50), ('Python', 100)])

Keys must be unique. A later key, value pair will overwrite an earlier
key, value pair that had the same key:

.. nbplot::

    >>> software = {'MATLAB': 50, 'Python': 100, 'MATLAB': 45}
    >>> software.items()  # doctest: +SKIP
    dict_items([('MATLAB', 45), ('Python', 100)])

*********
Functions
*********

Here we define our first function in Python:

.. nbplot::

    >>> def my_function(an_argument):
    ...     return an_argument + 1

The function definition begins with the ``def`` keyword followed by a
space. There follows the name of the function ``my_function``. Next we
have an open parenthesis, followed by a specification of the arguments
that the function expects to be passed to it. In this case, the function
expects a single argument. The value of this argument will be attached
to the name ``an_argument`` when the function starts to execute. Last,
we have an indented block, with code that will run when the function is
called. We return a value from the function using the ``return``
statement.

.. nbplot::

    >>> my_function(10)
    11

We called ``my_function`` by appending the opening parenthesis, and the
arguments, followed by the closing parenthesis. The function began to
execute with the variable ``an_argument`` set to 10. It returned 10 + 1
= 11.

A function need not accept any arguments:

.. nbplot::

    >>> def my_second_function():
    ...     return 42
    ...
    >>> my_second_function()
    42

A function can have more than one argument:

.. nbplot::

    >>> def my_third_function(first_argument, second_argument):
    ...     return first_argument + second_argument
    ...
    >>> my_third_function(10, 42)
    52

Remember that everything in Python is an object. The function is itself
an object, where the name of the function is a variable, that refers to
the function:

.. nbplot::

    >>> my_third_function
    <function my_third_function at 0x...>

.. nbplot::

    >>> type(my_third_function)
    <class 'function'>

We call the function by adding the open parenthesis, and the arguments
and the close parenthesis:

.. nbplot::

    >>> my_third_function(10, 42)
    52

We can make a new name to point to this same function as easily as we
can do this with other Python variables, such as lists:

.. nbplot::

    >>> another_reference_to_func3 = my_third_function
    >>> type(another_reference_to_func3)
    <class 'function'>

.. nbplot::

    >>> # We can call this function using the new name
    >>> another_reference_to_func3(10, 42)
    52

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

Sometimes you have more complicated objects to sort, for which you
cannot use ``<`` or ``>`` to compare the elements (maybe the greater
than or less than methods don't exist for this object). Sometimes your
objects do allow ``<`` or ``>`` but you want to order the objects in
some other way. If so, then you can define a *sort function*, that, when
given an element, returns a sort value for that element. Python does the
sorting, not on the elements themselves, but on the returned sort value
for each element.

For example, let's say you have three tuples that you want to sort:

.. nbplot::

    >>> tuples = (('c', 12), ('d', 13), ('b', 14))

Python does know how to compare tuples, by comparing the first value
first, then the second value, and so on. Because ``c`` is later in the
alphabet than ``b``, this means that:

.. nbplot::

    >>> ('c', 12) > ('b', 14)
    True

.. nbplot::

    >>> sorted(tuples)
    [('b', 14), ('c', 12), ('d', 13)]

That may not be what I want. I might want to sort by the second value in
the tuples, the numbers, rather than the first values - the strings. In
that case I can make a sort function, that accepts the element as an
input (the tuple in this case), and returns a value:

.. nbplot::

    >>> def by_number(element):
    ...     # The value we will return for this element
    ...     value = element[1]
    ...     # Show the value we will return
    ...     print('Returning sort value {} for element {}'.format(value, element))
    ...     return value

Remember everything in Python is an object. The function we have just
defined is also an object, with name ``by_number``:

.. nbplot::

    >>> by_number
    <function by_number at 0x...>

We can pass this value to the ``sorted`` function as a sort function:

.. nbplot::

    >>> sorted(tuples, key=by_number)
    Returning sort value 12 for element ('c', 12)
    Returning sort value 13 for element ('d', 13)
    Returning sort value 14 for element ('b', 14)
    [('c', 12), ('d', 13), ('b', 14)]
