##################
Introducing nipype
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

After this has run, check that you can import nipype with:

.. nbplot::

    >>> import nipype

We are interested in the nipype ``interfaces`` sub-package.  Specifically, we
want the interfaces to the SPM routines:

.. nbplot::

    >>> from nipype.interfaces import spm

Our first job is to make sure that nipype can run MATLAB. Let's check with a
test call:

.. nbplot::
    :render-parts: (0, 1)
    :run-parts: (0, 1) if have_matlab else 0

    >>> import nipype.interfaces.matlab as nim
    >>> mlab = nim.MatlabCommand()

    .. part

    >>> mlab.inputs.script = "version"  # get MATLAB version
    >>> mlab.run()
    <...>

If ``nipype`` does not have the right command to start MATLAB, this will fail
with an error. We can set the command to start MATLAB like this:

.. nbplot::

    >>> nim.MatlabCommand.set_default_matlab_cmd('/Applications/MATLAB_R2014a.app/bin/matlab')

where ``/Applications/MATLAB_R2014a.app/bin/matlab`` is the path to the MATLAB
application file.

Check this is working by running the code above.

Next we need to make sure that nipype has SPM on the MATLAB path when it
is running MATLAB. Try running this command to get the SPM version.

.. nbplot::
    :run-parts: 0 if have_spm else ()

    >>> mlab = nim.MatlabCommand()
    >>> mlab.inputs.script = "spm ver"  # get SPM version
    >>> mlab.run()
    <...>

If this gives an error message, you may not have SPM set up on your MATLAB
path by default. You can use Nipype to add SPM to the MATLAB path like this:

.. nbplot::

    >>> nim.MatlabCommand.set_default_paths('/Users/mb312/dev_trees/spm12')

Another option is to use the MATLAB GUI to add this directory to the MATLAB
path, and save this path for future sessions.

Now try running the ``spm ver`` command again:

.. nbplot::
    :run-parts: 0 if have_spm else ()

    >>> mlab = nim.MatlabCommand()
    >>> mlab.inputs.script = "spm ver"  # get SPM version
    >>> mlab.run()
    <...>

We are going to put the setup we need into a Python file we can import from
any script that we write that uses nipype.

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
    :run-parts: 0 if have_spm else ()

    >>> import nipype_settings
    >>> import nipype.interfaces.matlab as nim
    >>> mlab = nim.MatlabCommand()
    >>> mlab.inputs.script = "spm ver"  # get SPM version
    >>> mlab.run()
    <...>

These should run without error.
