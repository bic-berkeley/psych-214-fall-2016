###################################
Where does Python look for modules?
###################################

See:

* `Python docs on sys.path <https://docs.python.org/3.5/library/sys.html#sys.path>`_;
* `Python Module of the Week on: Import Path
  <https://pymotw.com/3/sys/imports.html#import-path>`_.

.. nbplot::
    :include-source: false

    >>> # - compatibility with Python 2
    >>> from __future__ import print_function, division

Let's say we have written a Python module and saved it as ``a_module.py``, in
a directory called ``code``.

We also have a script called ``a_script.py`` in a directory called
``scripts``.

We want to be able to ``import`` the code in ``a_module.py`` to use in
``a_script.py``.  So, we want to be able to put his line in
``a_script.py``::

    import a_module

The module and script might look like this:

.. workrun::
    :hide:

    rm -rf code scripts
    mkdir code scripts

.. writefile:: code/a_module.py
    :cwd: /working

    def func():
        print("Running useful function")

.. writefile:: scripts/a_script.py
    :cwd: /working

    import a_module

    a_module.func()

At the moment, ``a_script.py`` will fail with:

.. workrun::
    :allow-fail:

    python3 scripts/a_script.py

When Python hits the line ``import a_module``, it tries to find a package or a
module called ``a_module``.  A package is a directory containing modules, but
we will only consider modules for now.  A module is a file with a matching
extension, such as ``.py``.  So, Python is looking for a file ``a_module.py``,
and not finding it.

You will see the same effect at the interactive Python console, or in
IPython:

.. runblock::  pycon
    :cwd: /working

    >>> import a_module

**************************************
Python looks for modules in "sys.path"
**************************************

Python has a simple algorithm for finding a module with a given name, such as
``a_module``.  It looks for a file called ``a_module.py`` in the directories
listed in the variable ``sys.path``.

.. runblock::  pycon
    :cwd: /working

    >>> import sys
    >>> type(sys.path)
    >>> for path in sys.path:
    ...     print(path)

The ``a_module.py`` file is in the ``code`` directory, and this directory is
not in the ``sys.path`` list.

Because ``sys.path`` is just a Python list, like any other, we can make the
import work by appending the ``code`` directory to the list.

.. runblock::  pycon
    :cwd: /working

    >>> import sys
    >>> sys.path.append('code')
    >>> # Now the import will work
    >>> import a_module

There are various ways of making sure a directory is always on the Python
``sys.path`` list when you run Python, including:

* put the directory into the contents of the ``PYTHONPATH`` environment
  variable |--| :doc:`using_pythonpath` (see: :doc:`path_manipulation`) (see:
  :doc:`path_manipulation`):
* make the module part of an installable package, and install it |--| see:
  `making a Python package`_.

You can also put your ``code`` directory on the Python ``sys.path`` at the top
of the files that need it.  For example (see: :doc:`path_manipulation``):

::

    import sys
    sys.path.append('/Users/mb312/pna_code')

Is there any easier way?

Why yes - there is. In fact there are several.

The one we are going to use is the ``PYTHONPATH`` environment variable
(see https://docs.python.org/2/using/cmdline.html#envvar-PYTHONPATH).

If you are on a Mac
===================

-  Open ``Terminal.app``;
-  Open the file ``~/.bash_profile`` in your text editor;
-  Add the following line to the end:

   ::

       export PYTHONPATH=$HOME/pna_code

Save the file. \* Close ``Terminal.app``; \* Start ``Terminal.app``
again, and type this:

::

    ```
    echo $PYTHONPATH
    ```

It should show something like ``/Users/your_username/pna_code``. If not,
come get one of us.

If you are on Linux
===================

-  Open your favorite terminal program;
-  Open the file ``~/.bashrc`` in your text editor;
-  Add the following line to the end:

   ::

       export PYTHONPATH=$HOME/pna_code

   Save the file.
-  Close your terminal application;
-  Start your terminal application again, and type this:

   ::

       echo $PYTHONPATH

It should show something like ``/home/your_username/pna_code``. If not,
come get one of us.

If you are on Windows
=====================

Got to the Windows menu, right-click on "Computer" and select
"Properties":

From the computer properties dialog, select "Advanced system settings"
on the left:

From the advanced system settings dialog, choose the "Environment
variables" button:

In the Environment variables dialog, click the "New" button in the top
half of the dialog, to make a new *user* variable:

Give the variable name as ``PYTHONPATH`` and the value is the path to
the ``pna_code`` directory. Choose OK and OK again to save this
variable.

Now open a ``cmd`` Window (Windows key, then type ``cmd`` and press
Return). Type:

::

    echo %PYTHONPATH%

to confirm the environment variable is correctly set:

If you want the IPython notebook to see this new ``PYTHONPATH``
variable, you may need to close your terminal, open it again, and
restart ``ipython notebook``, so that it picks up ``PYTHONPATH`` from
the environment settings.

You can check the current setting of environment variables, using the
``os.environ`` dictionary:

.. nbplot::

    >>> import os
    >>> # os.environ['PYTHONPATH']  # doctest: +SKIP
