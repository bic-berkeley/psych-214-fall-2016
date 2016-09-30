################
Using PYTHONPATH
################

``PYTHONPATH`` is an :term:`environment variable`.

See the `Python 3 docs for PYTHONPATH
<https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH>`_.

The PYTHONPATH variable has a value that is a string with a list of
directories that Python should add to the :ref:`sys.path <sys-path>` directory
list.

The main use of PYTHONPATH is when we are developing some code that we want to
be able to import from Python, but that we have not yet made into an
installable Python package (see: `making a Python package`).

Returning to the example module and script in :doc:`sys_path`:

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

At the moment, on my machine, PYTHONPATH is empty:

.. workrun::

    echo $PYTHONPATH

Before we set PYTHONPATH correctly, ``a_script.py`` will fail with:

.. workrun::
    :allow-fail:

    python3 scripts/a_script.py

Now I set the PYTHONPATH environment variable value to be the path to the
``code`` directory:

.. workrun::

    # Set PYTHONPATH to path to the working directory + /code
    # This is for the "bash" shell on Unix / git bash on Windows
    export PYTHONPATH="$PWD/code"
    # Now the script can find "a_module"
    python3 scripts/a_script.py

***********************************
Setting PYTHONPATH more permanently
***********************************

You probably don't want to have to set PYTHONPATH every time you start up a
terminal and run a Python script.

Luckily, we can make the PYTHONPATH value be set for any terminal session, by
setting the environment variable default.

For example, let's say I wanted add the directory ``/Users/my_user/code`` to
the PYTHONPATH:

If you are on a Mac
===================

-  Open ``Terminal.app``;
-  Open the file ``~/.bash_profile`` in your text editor |--| e.g. ``atom
  ~/.bash_profile``;
-  Add the following line to the end:

   ::

       export PYTHONPATH="/Users/my_user/code"

Save the file.

* Close ``Terminal.app``;
* Start ``Terminal.app`` again, to read in the new settings, and type this:

    ::

        echo $PYTHONPATH

It should show something like ``/Users/my_user/code``.

If you are on Linux
===================

* Open your favorite terminal program;
* Open the file ``~/.bashrc`` in your text editor |--| e.g. ``atom
  ~/.bashrc``;
* Add the following line to the end:

   ::

       export PYTHONPATH=/home/my_user/code

  Save the file.
* Close your terminal application;
* Start your terminal application again, to read in the new settings, and
  type this:

   ::

       echo $PYTHONPATH

It should show something like ``/home/my_user/code``.

If you are on Windows
=====================

Got to the Windows menu, right-click on "Computer" and select "Properties":

From the computer properties dialog, select "Advanced system settings" on the
left:

From the advanced system settings dialog, choose the "Environment variables"
button:

In the Environment variables dialog, click the "New" button in the top half of
the dialog, to make a new *user* variable:

Give the variable name as ``PYTHONPATH`` and the value is the path to
the ``code`` directory. Choose OK and OK again to save this
variable.

Now open a ``cmd`` Window (Windows key, then type ``cmd`` and press
Return). Type:

::

    echo %PYTHONPATH%

to confirm the environment variable is correctly set.

If you want your IPython sessions to see this new ``PYTHONPATH`` variable,
you'll have to restart your terminal and restart IPython so that it picks up
``PYTHONPATH`` from the environment settings.

Checking system environment variables in Python
===============================================

You can check the current setting of environment variables, using the
``os.environ`` dictionary.   It contains all the defined environment variables
of the shell that started Python. For example, you can check the value of the
PYTHONPATH environment variable, if it is defined:

.. nbplot::
    :include-source: false

    >>> import os
    >>> os.environ['PYTHONPATH'] = "/home/my_user/code"

.. nbplot::

    >>> import os
    >>> os.environ['PYTHONPATH']
    '/home/my_user/code'
