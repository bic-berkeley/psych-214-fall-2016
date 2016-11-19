***********************
Packages and namespaces
***********************

Here is an example of *importing* a package:

.. nbplot::

    >>> import numpy as np

This Python code *imports* the *module* called ``numpy`` and gives it the new
name ``np``.

What ``type()`` of thing is ``np`` now?

.. nbplot::

    >>> type(np)
    <class 'module'>

A module contains stuff with *names*. For example, numpy contains a *function*
named ``sqrt``:

.. nbplot::

    >>> np.sqrt
    <ufunc 'sqrt'>

Because a module contains stuff with names, it is a *namespace*.

Numpy is also a *package* because it is a set of modules that get installed
together. For example, after you have installed numpy, you not only have the
``numpy`` module, but other submodules such as ``numpy.linalg``, for linear
algebra on numpy arrays:

.. nbplot::

    >>> import numpy.linalg as npl
    >>> type(npl)
    <class 'module'>

In IPython, try tab completing on ``npl.`` (``npl`` followed by a period -
``.``) to see what is in there.

Numpy is the module that contains the basic routines for creating and working
with 1D and 2D and 3D - and in fact ND arrays in Python. Almost every
scientific computing package in Python uses numpy.

We will be using two other packages for the exercises - ``matplotlib`` and
``nibabel``. Both of these packages depend heavily on numpy for working with
arrays.

Matplotlib is the standard Python package for doing high-quality plots.  The
original author wrote matplotlib to be similar to MATLAB (hence the name).

The best module for standard use is ``matplotlib.pyplot`` and we will import
it like this:

.. nbplot::

    >>> import matplotlib.pyplot as plt
    >>> type(plt)
    <class 'module'>

Lastly, we will be using the ``nibabel`` package for loading neuroimaging
format images:

.. nbplot::

    >>> import nibabel as nib

************
Getting help
************

If you don't know how to do a particular task in Python / Numpy /
Matplotlib, then try these steps:

* In IPython, do tab completion in the module, and have a look around.  For
  example, if you are looking for a routine to do rounding on arrays, then
  type ``np.ro`` followed by and you will see ``np.round`` as one of the
  suggestions;
* In IPython, get the help for particular functions or classes with the
  question mark at the end of the function or class name * e.g.  ``np.round?``
  followed by the Return key;
* In numpy or scipy (we'll come across scipy later), you can find stuff using
  ``lookfor``. For example, let's say you hadn't guessed that ``np.sqrt`` was
  the square root function in numpy, you could try ``np.lookfor('square
  root')``.
* Do a web search : http://lmgtfy.com/?q=numpy+square+root
