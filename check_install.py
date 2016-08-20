""" Test installation of packages for psych-214 class

Run with::

    python3 check_install.py

These programs should be installed:

* python 3 version >= 3.4
* git
* atom
* apm
* pip3 >= 8.1

The following packages should be installed:

* numpy
* scipy
* matplotlib
* nibabel
* ipython
* jupyter
"""

import sys
from subprocess import check_output, Popen, PIPE
from distutils.version import LooseVersion

# Python running us is >= 3.4
assert sys.version_info[:2] >= (3, 4)

# git on the command line
assert check_output(['git', '--version']).startswith(b'git version')

# Atom from the command line.  Raises FileNotFoundError if missing
atom_proc = Popen(['atom', '-h'], stdout=PIPE, stderr=PIPE)
out, err = atom_proc.communicate()
assert err == b''

# apm should be on the command line
assert check_output(['apm', '--version', '--color', 'false']).startswith(b'apm')

# pip on Python sys path should be >= 8.1
import pip
assert LooseVersion(pip.__version__) >= '8.1'

# Pip on shell path likewise
pip_cmd_out = check_output(['pip3', '--version']).split()
assert pip_cmd_out[0] == b'pip'
assert LooseVersion(pip_cmd_out[1].decode('latin1')) >= '8.1'

# Check the imports
import numpy
import scipy
import matplotlib
import nibabel
import IPython
import jupyter

print("Congratulations, all checks passed")
