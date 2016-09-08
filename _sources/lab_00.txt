######
Lab 00
######

Make sure you have read and understood * :doc:`brisk_python`.

Next fetch the exercises using the ``git clone`` command below.  The exercises
are slightly modified versions of the exercises from the `Google Python
class`_.  Specifically, the edited versions run correctly on Python 3.

::

    git clone https://github.com/psych-214-fall-2016/day_00_lab
    cd day_00_lab

Check that all is well by running the test program::

    python3 hello.py

Next get ready to start the `basic exercises`_::

    cd basic

First do these exercises:

* ``list1.py``;
* ``list2.py``;
* ``string1.py``;
* ``string2.py``.

To do the exercises:

* open IPython_ (``ipython`` at the terminal command line);
* in IPython, type ``run list1.py`` (or ``list2.py`` etc).  This will run the
  tests embedded in the exercise.  These should fail until you have edited the
  file to add the code you need;
* open ``list1.py`` (etc) in Atom;
* look at the instructions in the file, and fill out the functions that the
  instructions suggest.  Rerun ``run list.py`` in IPython when you've finished
  a function, to see whether the tests pass.

Now you are ready for the more extended exercises in ``wordcount.py`` and
``mimic.py``.  To test ``wordcount.py``, do::

    run wordcount.py --count small.txt

and::

    run wordcount.py --topcount small.txt

in IPython.  See the instructions in ``wordcount.py`` for the meaning of
``--count`` and ``--topcount``.  You might also try using ``alice.txt``
instead of ``small.txt``.

For ``mimic.py`` use::

    run mimic.py small.txt

in IPython.
