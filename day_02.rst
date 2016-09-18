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

****************************************
Introduction to the diagnostics exercise
****************************************

* reading bytes from a file;
* calculating a hash from the bytes.

See :ref:`reading-git-objects`.

* stripping and splitting strings:
* raising Errors;
* manipulating paths;
* `if __name__ == '__main__'
  <https://docs.python.org/3/library/__main__.html>`_;

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

* First half of chapter 8 of Huettel et al 2014 :cite:`huettel2014functional`.
* Exercises on array and images.
