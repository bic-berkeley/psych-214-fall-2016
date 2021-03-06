****************************************
Making and breaking file paths in Python
****************************************

See: https://docs.python.org/3.5/library/os.path.html

* ``os.path``
* ``dirname, basename, join, splitext, abspath``

.. nbplot::

    >>> import os.path

In IPython, you can tab complete on ``os.path`` to list the functions and
attributes there.

The first function we will use from ``os.path`` is ``dirname``.  To avoid
typing ``os.path.dirname`` all the time, import the ``dirname`` function
directly into the current name-space, by using the ``from module import ...``
version of the ``import`` command:

.. nbplot::

    >>> from os.path import dirname
    >>> dirname
    <function dirname at 0x...>

    >>> # This gives "os.path.dirname" the name "dirname"
    >>> os.path.dirname
    <function dirname at 0x...>
    >>> dirname is os.path.dirname
    True

The ``dirname`` function gives the directory name from a full file path. It
works correctly for Unix paths on Unix machines, and Windows paths on Windows
machines:

.. nbplot::

    >>> # On Unix
    >>> dirname('/a/full/path/then_filename.txt')
    '/a/full/path'

.. note:: Windows, backslash and strings

    On Windows, we have the extra problem that Python uses the backslash character
    in strings to indicate a special character follows.  For example the string
    ``"Tab \t, newline \n"`` contains a tab character and a newline character,
    indicated by ``"\t"`` and ``"\n"``.  So we need to prepend a backslash to
    each backslash we want in the output string:

::

    >>> # On Windows
    >>> dirname('c:\\a\\full\\path\\then_filename.txt') # doctest: +SKIP
    'c:\\a\\full\\path'

``dirname`` also works for relative paths,  A relative path where the starting
directory is relative to the current directory, rather than absolute, in terms
of the root of the file system:

.. nbplot::

    >>> # On Unix
    >>> dirname('relative/path/then_filename.txt')
    'relative/path'

Use ``basename`` to get the filename rather than the directory name:

.. nbplot::

    >>> from os.path import basename
    >>> # On Unix
    >>> basename('/a/full/path/then_filename.txt')
    'then_filename.txt'

Sometimes you want to join one or more directory names with a filename to get
a path.   Windows and Unix have different characters to separate directories
in a path.  Windows uses the backslash: ``\``, Unix uses a forward slash:
``/``.  If your code will run on Windows and Unix, you need to take care that
you get the right character joining your paths.  This is what ``os.path.join``
does:

.. nbplot::

    >>> from os.path import join
    >>> # On Unix
    >>> join('relative', 'path', 'then_filename.txt')
    'relative/path/then_filename.txt'

This also works on Windows::

    >>> # On Windows
    >>> join('relative', 'path', 'then_filename.txt')  # doctest: +SKIP
    'relative\\path\\then_filename.txt'

To convert a relative to an absolute path, use ``abspath``:

.. nbplot::

    >>> from os.path import abspath
    >>> # Show the current working directory
    >>> os.getcwd()  #doctest: +SKIP
    /Users/mb312/dev_trees/psych-214-fall-2016
    >>> abspath('relative/path/then_filename.txt')  #doctest: +SKIP
    /Users/mb312/dev_trees/psych-214-fall-2016/relative/path/then_filename.txt

Use ``splitext`` to split a path into: the path + filename; and the file
extension:

.. nbplot::

    >>> from os.path import splitext
    >>> splitext('relative/path/then_filename.txt')
    ('relative/path/then_filename', '.txt')
