##################
Introducing Nipype
##################

.. nbplot::
    :include-source: false

    >>> # compatibility with Python 2
    >>> from __future__ import print_function
    >>> from __future__ import division

`Nipype`_ is a Python module that provides Python interfaces to many imaging
tools, including SPM, AFNI and FSL.

We install it with ``pip`` in the usual way::

    pip3 install --user nipype

After this has run, check that you can import Nipype with:

.. nbplot::

    >>> import nipype

We are interested in the Nipype ``interfaces`` sub-package.  Specifically, we
want the interfaces to the SPM routines:

.. nbplot::

    >>> from nipype.interfaces import spm

Our first job is to make sure that Nipype can run MATLAB. Let's check with a
test call:

.. nbplot::
    :run-parts: () if not have_matlab else 0

    >>> import nipype.interfaces.matlab as nim
    >>> mlab = nim.MatlabCommand()
    >>> mlab.inputs.script = "version"  # get MATLAB version
    >>> mlab.run()
    <...>

If Nipype does not have the right command to start MATLAB, this will fail with
an error. We can set the command to start MATLAB like this:

.. nbplot::

    >>> nim.MatlabCommand.set_default_matlab_cmd('/Applications/MATLAB_R2014a.app/bin/matlab')

Check this is working by running the code above.

Next we need to make sure that Nipype has SPM on the MATLAB path when it
is running MATLAB. Try running this command to get the SPM version.

.. The following assumes that, if MATLAB is on the path, then it also has SPM
   on the MATLAB path.

.. nbplot::
    :run-parts: () if not have_matlab else 0

    >>> mlab = nim.MatlabCommand()
    >>> mlab.inputs.script = "spm ver"  # get SPM version
    >>> mlab.run()
    <...>

If this gives an error message, you may not have SPM set up on your MATLAB
path by default. You can add SPM to the MATLAB path like this:

.. nbplot::

    >>> nim.MatlabCommand.set_default_paths('/Users/mb312/dev_trees/spm12')

Now try running the ``spm ver`` command again:

.. nbplot::
    :run-parts: () if not have_matlab else 0

    >>> mlab = nim.MatlabCommand()
    >>> mlab.inputs.script = "spm ver"  # get SPM version
    >>> mlab.run()
    <...>

We are going to put the setup we need into a Python file we can import from
any script that we write that uses Nipype.

In your current directory, make a new file called ``nipype_settings.py`` with
contents like this::

    """ Defaults for using nipype
    """
    import nipype.interfaces.matlab as nim
    # If you needed to set the default matlab command above
    nim.MatlabCommand.set_default_matlab_cmd('/Applications/MATLAB_R2014a.app/bin/matlab')
    # If you needed to set the SPM path above
    nim.MatlabCommand.set_default_paths('/Users/mb312/dev_trees/spm12')

Now try:

.. nbplot::
    :run-parts: () if not have_matlab else 0

    >>> import nipype_settings
    >>> import nipype.interfaces.matlab as nim
    >>> mlab = nim.MatlabCommand()
    >>> mlab.inputs.script = "spm ver"  # get SPM version
    >>> mlab.run()
    <...>

These should run without error.
