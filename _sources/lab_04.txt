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

``np.logical_and``, ``np.logical_or``:

.. nbplot::

    >>> import numpy as np

    >>> bool1 = np.array([True, True, False, False])
    >>> bool2 = np.array([False, True, False, True])

    >>> # logical_and True where both of bool1 and bool2 are True
    >>> np.logical_and(bool1, bool2)
    array([False,  True, False, False], dtype=bool)

    >>> # logical_or True where either of bool1 and bool2 are True
    >>> np.logical_or(bool1, bool2)
    array([ True,  True, False,  True], dtype=bool)

****************
Some live coding
****************

With guest editor Stéfan van der Walt:

* making issues;
* feature branches;
* pull requests;
* responding to comments on pull requests;
* merging pull requests with the "Merge" button on Github.

.. _git-workflow-exercises:

************
Git workflow
************

spm_funcs exercise
==================

* Fork the repository at https://github.com/psych-214-fall-2016/outlier-utils;
* Clone your fork;
* Make a *new branch to work on*;
* Solve the ``code/spm_funcs.py`` exercise;
* Commit;
* Push;
* Make a pull request back to https://github.com/psych-214-fall-2016/outlier-utils.

detector exercise
=================

* Make a *new branch to work on*;
* Solve the ``code/detectors.py`` exercise;
* Commit;
* Push;
* Make a pull request back to https://github.com/psych-214-fall-2016/outlier-utils.
