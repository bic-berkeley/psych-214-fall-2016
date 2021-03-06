###################
Modules and scripts
###################

.. nbplot::
    :include-source: false

    >>> # Compatibility with Python 
    >>> from __future__ import print_function
    >>> from __future__ import division  # 1/2 == 0.5, not 0

.. nbplot::

    >>> #: Usual imports
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> import nibabel as nib

Let's say I have a function that loads a 4D image, and returns a list with
mean values across all voxels in each volume:

.. nbplot::

    >>> def vol_means(image_fname):
    ...     img = nib.load(image_fname)
    ...     data = img.get_data()
    ...     means = []
    ...     for i in range(data.shape[-1]):
    ...         vol = data[..., i]
    ...         means.append(np.mean(vol))
    ...     return means

First we check that works:

.. nbplot::

    >>> my_means = vol_means('ds107_sub012_t1r2.nii')
    >>> plt.plot(my_means)
    [...]

That seems like a useful function to me. I want to make a module called
``mymodule`` so I can do this in some Python script or at the IPython prompt:

::

    import mymodule
    means = mymodule.vol_means('ds107_sub012_t1r2.nii')

In fact, what I would really like to do, is to be able to have a script called
``my_script.py`` that prints the scan means out to the terminal window like
this:

::

    import mymodule

    means = mymodule.vol_means('ds107_sub012_t1r2.nii')
    for mean in means:
        print(mean)

And I want to be able to run it like this from the command line:

::

    python my_script.py

A Python *module* is a Python file with functions (and variables and other
things) that other modules and scripts may use. These other modules and
scripts will ``import`` the module.

A script is a file that you can run with ``python3 my_script.py``. The script
will usually do some processing, and may print something to the terminal, put
up a plot or save some data to the filesystem.

You store modules in text files ending in ``.py``. For example, the module
``mymodule`` would be in a file called ``mymodule.py``.

A module needs to ``import`` everything it uses.

You can store scripts with any extension, but it is common to use ``.py``
extensions for Python scripts as well.

*********************************
The __name___ == "__main__" trick
*********************************

You can execute a module in two different contexts:

* execute as a script (``python3 my_script.py``);
* import as a module (``>>> import my_script``).

It is reasonably common to want to use your ``.py`` file in either of these
two ways.  For example, you may want to use and debug the functions in your
code after ``>>> import my_script``, and then run the code as a script with
``python3 my_script.py``.

How does a Python file know whether it is being executed as a script or
imported as a module?

To help with this problem, Python sets a variable that tells you whether you
are currently being ``import``-ed or not.   This is the ``__name__`` variable.

Notice the double underscores on either side of the variable name.  Variables
with double underscores on either side are often referred to as "dunder"
variables (for Double UNDERscore).  When Python is going to set or use a
variable or method name for its own purposes, it usually uses a dunder name,
as here.

For our purposes ``__name__ == "__main__"`` if our Python file is running as a
script and ``__name__`` is set to the module name if the module is being
imported.  For example, if we did ``import my_script``, then, when
``my_script.py`` gets run, ``__name__`` will be set to ``my_script``.

When you do want to use your ``.py`` file as a script, or for importing, you
often see this pattern at the bottom of the ``.py`` file::

    def main():
        # Only run this function when used as a script
        # The name "main" is only a common convention, the function could have
        # any name.


    if __name__ == '__main__':
        # We only get here if running the file as a script
        main()

See `if __name__ == '__main__'
<https://docs.python.org/3/library/__main__.html>`_ in the Python
documentation.

**********************
Command line arguments
**********************

When you run a script, you can also pass command line arguments, e.g.::

    python3 my_script.py a_string

Here ``my_script.py`` is the script, and ``a_string`` is the command line
argument.

You can do the same thing from within IPython::

    run my_script.py a_string

In your script, you can get the command line arguments from the ``argv``
list within the ``sys`` module.  The first element of the ``sys.argv`` list is
always the name of the program |--| in our case this will be ``my_script.py``.
The second and subsequent entries in ``sys.argv`` are the arguments entered at
the command line.  For example, in our case::

    sys.argv == ['my_script.py', 'a_string']

The entries in this list are always strings.  For ``python3 my_script.py 1``
you would get::

    sys.argv == ['my_script.py', '1']

*************
Example files
*************

Example files at:

* :download:`mymodule.py`;
* :download:`my_script.py`.
