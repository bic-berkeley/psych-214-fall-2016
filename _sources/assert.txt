############################
Using ``assert`` for testing
############################

The Python ``assert`` statement means - "raise an error unles the following
expression is equivalent to True".

By "equivalent to True", I mean the expression returns True from Python `truth
value testing`_.  See :ref:`equivalent-to-true` for more.

``assert`` raises an ``AssertionError`` if the statement is equivalent to
False.  It does nothing if the statement is equivalent to True.

So, if you ``assert an_expression`` and there is no error, then the result of
``an_expression`` was equivalent to True.  The following expressions evaluate
to True, and therefore the asserts do not raise an error:

>>> assert True
>>> assert 10 == 10
>>> assert 10 % 2 == 0

These expressions are equivalent to False, and the asserts do raise errors:

>>> assert False
Traceback (most recent call last):
   ...
AssertionError
>>> assert 10 == 11
Traceback (most recent call last):
   ...
AssertionError

.. _equivalent-to-true:

******************
Equivalent to True
******************

See: `truthiness in Python`_ and Python `truth value testing`_.

You can see the results of truth value testing using ``bool()`` in Python.
For example:

>>> bool(True)
True
>>> bool(False)
False
>>> bool(['some', 'elements'])  # not-empty list tests as True
True
>>> bool([])  # an empty list tests as False
False
>>> bool(10)  # any number other than zero evaluates as True
True
>>> bool(1)
True
>>> bool(0)
False
>>> bool(None)  # None tests as False
False

This is the truth testing that ``assert`` is using:

>>> assert ['some', 'elements']  # not-empty list tests as True
>>> assert []  # an empty list tests as False
Traceback (most recent call last):
   ...
AssertionError
>>> assert 10  # any number other than zero evaluates as True
>>> assert 1
>>> assert 0
Traceback (most recent call last):
   ...
AssertionError
>>> assert None
Traceback (most recent call last):
   ...
AssertionError
