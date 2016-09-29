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

See: https://docs.python.org/3.5/library/os.path.html

* ``os.path``
* ``dirname, basename, join, splitext, abspath``

*******************************
Adding stuff to the Python PATH
*******************************

The mystery of where ``mymodule`` comes from, when you do ``import mymodule``.

See: https://docs.python.org/3.5/library/sys.html#sys.path

*******
Testing
*******

* assert statements;

****************
Some numpy stuff
****************

* ``np.logical_and``, ``np.logical_or``;

****************
Some live coding
****************

With guest editor Stéfan van der Walt.

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
