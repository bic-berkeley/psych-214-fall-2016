#####################################################
September 19: version control, 4D arrays, diagnostics
#####################################################

*************************
4D arrays and time series
*************************

* Loading images with nibabel_;
* 4D images as collections of 3D images;
* getting volumes from 4D images;
* getting time-series from 4D images by slicing;

* intro page: :doc:`intro_to_4d`;
* exercise: :doc:`four_dimensions_exercise`.

*********************
Modules and functions
*********************

* intro :doc:`on_modules`.
* exercise::

    git clone https://github.com/psych-214-fall-2016/classwork
    cd classwork/day_02
    ipython

  then (in IPython)::

    run spm_funcs.py

****************************************
Introduction to the diagnostics exercise
****************************************

* reading bytes from a file;
* calculating a hash from the bytes.

See :ref:`reading-git-objects`.

* stripping and splitting strings with ``my_string.strip()`` and
  ``my_string.split()``;
* raising Errors with ``raise``;
* manipulating paths with ``os.path``.

Split into groups, then:

* Get the data for your group from the USB key(s);
* Tell me about your groups;
* "Fork" the repository for your group, to your github user:

    * Group 00 forks : https://github.com/psych-214-fall-2016/diagnostics-00
    * Group 01 forks : https://github.com/psych-214-fall-2016/diagnostics-01
    * Group 02 forks : https://github.com/psych-214-fall-2016/diagnostics-02

* Clone your forked repository.  For example::

    git clone https://github.com/matthew-brett/diagnostics-00
    git clone https://github.com/matthew-brett/diagnostics-00

  where ``matthew-brett`` is your github user name, and ``00`` is your group.

* Change directory into this new directory, e.g.::

    cd diagnostics-00

* Copy the data from the USB key into your new ``data`` directory;
* Run ``python3 scripts/validata_data.py data``
* Edit ``scripts/validate_data.py`` in Atom to fix.

**********************************
Reading and homework for next week
**********************************

Reading is chapter 8 of Huettel et al 2014 :cite:`huettel2014functional`.

Homework is to continue the diagnostics exercise.

You have two weeks to do this exercise.

Your goal is to:

#. Fill out the script and any needed library code to run
   ``scripts/find_outliers.py data`` on your data, and return a list of
   outlier volumes for each scan (where there is an outlier);
#. You should add a text file giving a brief summary for each outlier scan,
   why you think the detected scans should be rejected as an outlier, and your
   educated guess as to the cause of the difference between this scan and the
   rest of the scans in the run;
#. You should do this by collaborating in your teams using git and github;

Grading will be on:

* the quality of your outlier detection as assessed by the improvement in the
  statistical testing for the experimental model after removing the outliers;
* the generality of your outlier detection as assessed by the improvement in
  the statistical testing for the experimental model after removing the
  outliers, for another similar dataset;
* the quality of your code;
* the quality and transparency of your process, from your interactions on
  github;
* the quality of your arguments about the scans rejected as outliers.

We will cover more of the workflow in the Thursday lab.
