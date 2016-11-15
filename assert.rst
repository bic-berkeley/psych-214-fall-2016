############################
Using ``assert`` for testing
############################

The Python ``assert`` statement means - "raise an error unless the expression
that follows evaluates to True".

``assert`` raises an ``AssertionError`` if the statement evaluates to False.
It does nothing if the statement evaluates to True.

So, if you ``assert an_expression`` and there is no error, than
``an_expression`` evaluated to True.  All of the following expressions
evaluate to True, and therefore the asserts do not raise an error:

>>> assert True
>>> assert 10 == 10
>>> assert 10 % 2 == 0

But:

>>> assert False
Traceback (most recent call last):
   ...
AssertionError
>>> assert 10 == 11
Traceback (most recent call last):
   ...
AssertionError
