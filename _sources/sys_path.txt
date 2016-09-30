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

    rm -rf code scripts another_dir
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

.. _sys-path:

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
  variable |--| :doc:`using_pythonpath`
* make the module part of an installable package, and install it |--| see:
  `making a Python package`_.

As a crude hack, you can also put your ``code`` directory on the Python
``sys.path`` at the top of the files that need it:

.. writefile:: scripts/a_script_with_hack.py
    :cwd: /working

    import sys
    sys.path.append('code')

    import a_module

    a_module.func()

Then:

.. workrun::

    python3 scripts/a_script_with_hack.py

The simple ``append`` above will only work when running the script from a
directory containing the ``code`` subdirectory.  For example:

.. workrun::
    :allow-fail:

    mkdir another_dir
    cd another_dir
    python3 ../scripts/a_script_with_hack.py

This is because the directory ``code`` that we specified is a relative path,
and therefore Python looks for the ``code`` directory in the current working
directory.

To make the hack work when running the code from any directory, you could use
some :doc:`path manipulation <path_manipulation>` on the :ref:`file-variable`:

.. writefile:: scripts/a_script_with_better_hack.py
    :cwd: /working

    from os.path import dirname, abspath, join
    import sys

    # Find code directory relative to our directory
    THIS_DIR = dirname(__file__)
    CODE_DIR = abspath(join(THIS_DIR, '..', 'code'))
    sys.path.append(CODE_DIR)

    import a_module

    a_module.func()

Now the module import does work from ``another_dir``:

.. workrun::
    :cwd: /working/another_dir

    python3 ../scripts/a_script_with_better_hack.py
