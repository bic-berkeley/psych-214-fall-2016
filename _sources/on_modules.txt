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
    print(means)

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

A module needs to 'import' everything it uses.

You can store scripts with any extension, but it is common to use ``.py``
extensions for Python scripts as well.

Now let's go to the text editor and the terminal, and create the module
``mymodule.py`` and the script ``my_script.py``, with the contents from this
page.

Solutions at:

* :download:`mymodule.py`;
* :download:`my_script.py`.
