####################################
Introduction to Python for beginners
####################################

*********
Variables
*********

.. nbplot::

    >>> a = 4
    >>> b = 6

.. nbplot::

    >>> a + b
    10

.. nbplot::

    >>> a += 2
    >>> a
    6

.. nbplot::

    >>> a = "Python"
    >>> c = "MATLAB"
    >>> z = " > "
    >>> a + z + c
    'Python > MATLAB'

Strings can have quotes or double quotes, there's no difference in Python:

.. nbplot::

    >>> first = 'a string'
    >>> second = "b string"
    >>> first + second
    'a stringb string'

Length of a string:

.. nbplot::

    >>> len(first)
    8

Strings and numbers are different:

.. nbplot::

    >>> number = "9"
    >>> number + 6
    Traceback (most recent call last):
       ...
    TypeError: cannot concatenate 'str' and 'int' objects

We can convert between numbers and strings:

.. nbplot::

    >>> int(number) + 6
    15
    >>> str(9)
    '9'

However...

.. nbplot::

    >>> number = "nine"
    >>> int(number)
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: 'nine'

*****
Lists
*****

.. nbplot::

    >>> an_empty_list = []
    >>> list_with_two_items = [1, 2]
    >>> items_can_be_diverse = [1, "Obama", 4.55]

.. nbplot::

    >>> example_list = []
    >>> example_list.append("experiment1")
    >>> example_list
    ['experiment1']

.. nbplot::

    >>> example_list[0]
    'experiment1'

The length of a list (or any object that can have a length):

.. nbplot::

    >>> len(example_list)
    1

.. nbplot::

    >>> example_list.append("failed_experiment")
    >>> print(example_list)
    ['experiment1', 'failed_experiment']
    >>> example_list.append("failed_experiment")
    >>> print(example_list)
    ['experiment1', 'failed_experiment', 'failed_experiment']

.. nbplot::

    >>> example_list.pop()
    'failed_experiment'

.. nbplot::

    >>> example_list
    ['experiment1', 'failed_experiment']

.. nbplot::

    >>> del example_list[0]
    >>> example_list
    ['failed_experiment']

``range`` in Python 3 returns a "range object".  It's like a list, but isn't
quite a list.

.. nbplot::

    >>> range(10)
    range(0, 10)

You can make it into a list by using the ``list`` constructor.  A constructor
is like a function, but it creates a new object, in this case a new object of
type ``list``.

.. nbplot::
    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

You can also set the start element for ``range``:

.. nbplot::

    >>> list(range(2, 7))
    [2, 3, 4, 5, 6]

Use ``in`` to ask if a element is a collection of things, such as a range, or
a list:

.. nbplot::

    >>> 5 in range(2, 7)
    True
    >>> 5 in [2, 5, 7]
    True

.. nbplot::

    >>> 9 in range(2, 7)
    False

****
Sets
****

Sets are unordered, and unique.

"Unordered" means the order is arbitrary, and Python reserves the right to
return the elements in any order it likes:

.. nbplot::

    >>> our_work = set(["metacognition", "mindwandering", "perception"])
    >>> print(our_work)  # doctest: +SKIP
    {'mindwandering', 'perception', 'metacognition'}

If you want to get a version of the set that is ordered, use ``sorted``, which
returns a sorted list:

.. nbplot::

    >>> sorted(our_work)
    ['metacognition', 'mindwandering', 'perception']

You can't index a set, because the indices 0, or 1, or 2 don't correspond to
any particular element (because the set is unordered):

.. nbplot::

    >>> our_work[0]
    Traceback (most recent call last):
    ...
    TypeError: 'set' object does not support indexing

Add to a set with the ``add`` method:

.. nbplot::

    >>> our_work.add("consciousness")
    >>> print(our_work)  # doctest: +SKIP
    {'mindwandering', 'perception', 'metacognition', 'consciousness'}

.. nbplot::

    >>> our_work.add("consciousness")
    >>> print(our_work)  # doctest: +SKIP
    {'mindwandering', 'perception', 'metacognition', 'consciousness'}
    >>> our_work.add("consciousness")
    >>> print(our_work)  # doctest: +SKIP
    {'mindwandering', 'perception', 'metacognition', 'consciousness'}

You can subtract sets:

.. nbplot::

    >>> competing_labs_work = set(["motor control", "decision making", "memory", "consciousness"])
    >>> what_we_should_focus_on = our_work - competing_labs_work
    >>> print(what_we_should_focus_on)  # doctest: +SKIP
    {'mindwandering', 'perception', 'metacognition'}

.. nbplot::

    >>> what_we_should_avoid = our_work.intersection(competing_labs_work)
    >>> print(what_we_should_avoid)
    {'consciousness'}

Sets have lengths as well:

.. nbplot::

    >>> len(what_we_should_focus_on)
    3

*******
Strings
*******

.. nbplot::

    >>> example = "mary had a little lamb"
    >>> print(example)
    mary had a little lamb

String slicing:

.. nbplot::

    >>> example[0]
    'm'

.. nbplot::

    >>> example[0:4]
    'mary'

You can split strings with any character.  This breaks up the string,
returning a list of strings broken at the separator character:

.. nbplot::

    >>> example.split(" ")
    ['mary', 'had', 'a', 'little', 'lamb']

.. nbplot::

    >>> example.split(" ")[4]
    'lamb'

You can split with any character:

.. nbplot::

    >>> another_example = 'one:two:three'
    >>> another_example.split(":")
    ['one', 'two', 'three']

You can also ``strip`` a string.  That returns a new string with spaces, tabs
and end of line characters removed from the beginning and end:

.. nbplot::

    >>> my_string = ' a string\n'
    >>> my_string
    ' a string\n'
    >>> my_string.strip()
    'a string'

Adding strings:

.. nbplot::

    >>> example + " or two"
    'mary had a little lamb or two'

Putting strings into other strings:

.. nbplot::

    >>> subject_id = "sub1"
    >>> print("Subject {} is excellent".format(subject_id))
    Subject sub1 is excellent

.. nbplot::

    >>> age = 29
    >>> print("Subject {} is {} years old".format(subject_id, age))
    Subject sub1 is 29 years old

You can do more complex formatting of numbers and strings using formatting
options after a ``:`` in the placeholder for the string.  See:
https://docs.python.org/3.5/library/string.html#format-examples.

.. nbplot::

    >>> print("Subject {:02d} is here".format(4))
    Subject 04 is here

********
For loop
********

.. nbplot::

    >>> for i in range(10):
    ...     print(i)
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

Identation is crucial!

.. nbplot::

    >>> # for i in range(10):
    >>> # print(i)

Watch out for mistakes:

.. nbplot::

    >>> for i in range(10):
    ...     j = i + 1
    >>> print(j)
    10

**************
Ifs and breaks
**************

.. nbplot::

    >>> a = 2
    >>> b = 5
    >>> c = a + b
    >>> if c < 6:
    ...     print("yes")

.. nbplot::

    >>> if c < 6:
    ...     print("yes")
    ... else:
    ...     print("no")
    no

.. nbplot::

    >>> if c < 6:
    ...     print("yes")
    ... elif c > 6:
    ...     print("no")
    ... else:
    ...     print("kind of")
    no

.. nbplot::

    >>> if True:
    ...     print("true, true!")
    true, true!

.. nbplot::

    >>> if False:
    ...     print("never!")

.. nbplot::

    >>> for i in range(10):
    ...     if i == 6:
    ...         break
    ...     print(i)
    0
    1
    2
    3
    4
    5

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

*****
Logic
*****

You can use logical operators like ``and``, ``or`` and ``not``:

.. nbplot::

    >>> strange_election = True
    >>> uncomfortable_choices = True
    >>> satisfying_experience = False
    >>> strange_election and uncomfortable_choices
    True
    >>> strange_election and satisfying_experience
    False
    >>> strange_election and not satisfying_experience
    True

We often use these in ``if`` statements:

.. nbplot::

    >>> if strange_election and not satisfying_experience:
    ...     print('Watching a lot of news')
    Watching a lot of news

*****
Files
*****

Write lines to a text file:

.. nbplot::

    >>> fobj = open("/tmp/important_notes.txt", "wt")
    >>> type(fobj)
    <...>

.. nbplot::

    >>> fobj.write("captains log 672828: I had a banana for breakfast.\n")
    51
    >>> fobj.write("captains log 672829: I should watch less TV.\n")
    45
    >>> fobj.close()

Read lines from a text file:

.. nbplot::

    >>> fobj = open("/tmp/important_notes.txt", "rt")
    >>> print(fobj.readline())
    captains log 672828: I had a banana for breakfast.
    <BLANKLINE>
    >>> print(fobj.readline())
    captains log 672829: I should watch less TV.
    <BLANKLINE>

.. nbplot::

    >>> print(fobj.readline())
    <BLANKLINE>

Close a file when you've finished with it:

.. nbplot::

    fobj.close()

One way to read all the lines from a text file:

.. nbplot::
    >>> fobj = open("/tmp/important_notes.txt", "rt")
    >>> lines = fobj.readlines()
    >>> fobj.close()
    >>> len(lines)
    2
    >>> print(lines[0])
    captains log 672828: I had a banana for breakfast.
    <BLANKLINE>
    >>> print(lines[1])
    captains log 672829: I should watch less TV.
    <BLANKLINE>
