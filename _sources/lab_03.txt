###########################################
Outlier detection and git / github workflow
###########################################

***************
Getting started
***************

* Refresher on git and remotes;
* Clone, fetch, push, pull;
* Github, forks and remotes;

Call the central repository: "upstream".

See :ref:`diagnostics-preparation` to start.

If you have not done this already, you will need to start by:

* Fork your *upstream* repository (for group 00, 01 or 02) to your *user*
  using the github interface;
* Clone your user copy;
* ``git log``;
* Move the data into the repository (see :ref:`diagnostics-preparation`).

*********
Exercises
*********

* Go to your upstream repository web-page:

    * Group 00 : https://github.com/psych-214-fall-2016/diagnostics-00
    * Group 01 : https://github.com/psych-214-fall-2016/diagnostics-01
    * Group 02 : https://github.com/psych-214-fall-2016/diagnostics-02

* I make a pull request to each repository;
* Select the Pull Requests tab and have a look at the changes I've suggested.
  Merge them.
* On your machine, in your user repository directory, do ``git log``.  Has
  anything changed?
* Do ``git fetch origin``.  Has anything changed?
* Add a remote for your upstream repository, e.g.::

    git remote add upstream https://github.com/psych-214-fall-2016/diagnostics-00

* Check your remotes with ``git remote -v``;
* Fetch information about your new remote with ``git fetch upstream``;
* Make a new branch to work on, starting at the position of
  ``upstream/master``::

    git branch for-exercise-1 upstream/master

* Do exercise 1 (from my pull-request). Read the comments at the top of
  ``scripts/calc_dvars.py``.  If you're running at normal speed, just do the
  first past of the exercises listed there.  If you're rushing ahead, try the
  other problems.
* When done, use Git to commit your changes;
* Send this new branch up to your user repository on github.  Type::

    git push origin for-exercise-1:for-exercise-1 --set-upstream

* Use the github web interface to make a pull request from this new branch to
  your upstream repository;
* Go again to your upstream repository web page.  Review the new pull request.
  Merge.
* Fetch the merged changes from your upstream repository with::

    git fetch upstream
