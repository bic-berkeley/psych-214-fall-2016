#######################
Git and github workflow
#######################

*************************
What branch should I use?
*************************

* Never use ``master``;
* Make a new branch for each new bit of work.

*****************
Path manipulation
*****************

See: :doc:`path_manipulation`.

*******************************
Adding stuff to the Python PATH
*******************************

The mystery of where ``mymodule`` comes from, when you do ``import mymodule``.

See: :doc:`sys_path`.

*******
Testing
*******

Using assert statements:

>>> # No error
>>> assert True
>>> # Tests whether expression evaluates to True
>>> assert 10 == 10

>>> # Error
>>> assert False
Traceback (most recent call last):
   ...
AssertionError

>>> # Tests whether statement evaluates to True
>>> assert 10 == 11
Traceback (most recent call last):
   ...
AssertionError

****************
Some numpy stuff
****************

See: :doc:`numpy_logical`.

****************
Some live coding
****************

With guest editor Stéfan van der Walt:

* making issues;
* feature branches;
* pull requests;
* responding to comments on pull requests;
* merging pull requests with the "Merge" button on Github.

************
Git workflow
************

See: :doc:`git_workflow_exercises`.
