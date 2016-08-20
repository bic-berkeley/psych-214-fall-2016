#####################
Installation on Linux
#####################

*********************************
Installing Python 3, git and atom
*********************************

On Ubuntu or Debian
===================

Install git and Python 3:

.. code-block:: bash

    sudo apt-get update
    sudo apt-get install -y git python3-dev
    sudo apt-get install -y git

Check your Python 3 version with:

.. code-block:: bash

    python3 --version

This should give you a version >= 3.4.  If not, ask your instructors for help.

Install the ``wget`` command for downloading via the command line:

.. code-block:: bash

    sudo apt-get install -y wget

Point your web browser at the `atom releases`_ page and download the latest
``.deb`` file for your distribution.  Here's me downloading a recent release
from the command line:

.. code-block:: bash

    wget https://github.com/atom/atom/releases/download/v1.9.9/atom-amd64.deb

Install the Atom ``.deb`` package with:

.. code-block:: bash

    # This command will error with unmet dependencies
    sudo dpkg --install atom-amd64.deb
    # Fix the dependencies with this command
    apt-get -f install -y

On Fedora
=========

Install git and Python 3:

.. code-block:: bash

    sudo dnf install -y python3-devel git

If you get ``bash: dnf: command not found``, run ``sudo yum install dnf`` and
try again.

Check your Python 3 version with:

.. code-block:: bash

    python3 --version

This should give you a version >= 3.4.  If not, ask your instructors for help.

Install the ``wget`` command for downloading via the command line:

.. code-block:: bash

    sudo dnf install -y wget

Point your web browser at the `atom releases page`_ and download the latest
``.rpm`` file for your distribution.  Here's me downloading a recent release
from the command line:

.. code-block:: bash

    wget https://github.com/atom/atom/releases/download/v1.9.9/atom.x86_64.rpm

Install the Atom ``.rpm`` package with:

.. code-block:: bash

    sudo dnf install -y ./atom.x86_64.rpm

****************************
Installing Python 3 packages
****************************

To get ready for Python user installs, put the user local install ``bin``
directory on your system :term:`PATH`.  First find the path the user ``bin``
directory with:

.. code-block:: bash

    python3 -c 'import site; print(site.USER_BASE + "/bin")'

This will give you a result like ``/home/your_username/.local/bin``.

Open the ``~/.bashrc`` file in your home directory with Atom:

.. code-block:: bash

    atom ~/.bashrc

Add these lines to end of the file:

.. code-block:: bash

    # Put the path to the local bin directory into a variable
    py3_local_bin=$(python3 -c 'import site; print(site.USER_BASE + "/bin")')
    # Put the directory at the front of the system PATH
    export PATH="$py3_local_bin:$PATH"

Save the file, and restart your terminal to load the configuration from your
``~/.bashrc`` file.  Confirm that you have the ``.local/bin`` directory in
your PATH now:

.. code-block:: bash

    echo $PATH

Now install the Python package installer ``pip`` into your user directories
(see: `install pip with get-pip.py`_):

.. code-block:: bash

    # Download the get-pip.py installer
    wget https://bootstrap.pypa.io/get-pip.py
    # Execute the installer for Python 3 and a user install
    python3 get-pip.py --user

Check you now have the right version of the ``pip3`` command with:

.. code-block:: bash

    which pip3

This should give you something like ``/home/your_username/.local/bin/pip3``.

Finally, install the packages you need for the class:

.. code-block:: bash

    pip3 install --user numpy scipy matplotlib ipython nibabel jupyter

.. include:: links_names.inc
