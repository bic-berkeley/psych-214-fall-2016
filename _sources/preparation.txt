###########
Preparation
###########

We are going to be using the following major software for the class:

* Python_ 3 (see :ref:`why python?`);
* numpy_ (the Python array package);
* matplotlib_ (Python plotting package);
* scipy_ (Python scientific library);
* nibabel_ (read / write of neuroimaging file formats in Python);

For the class and homework we will use:

* the Aton_ text editor (see :ref:`why Atom?`);
* the hydrogen_ Atom plugin for interactive code;
* the git_ version control system.

See:

* :doc:`installation_on_mac`;
* :doc:`installation_on_linux`;

You will also need one of:

* MATLAB installed on your laptop or;
* an account on the `neuro cluster`_ (so you can run MATLAB / SPM_ remotely).

*************
Why Python 3?
*************

"Why Python 3?" is really two questions |--| "why Python?" and "why
Python version 3".

Python has become the standard language for open-source scientific computing.
It's an excellent language for teaching |--| see for example the `Berkeley
CS61A course <http://cs61a.org>`_ and the `MIT introduction to computer
science and programming
<http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/>`_.

The CS61A course notes have a good introduction to the `benefits of Python
<http://composingprograms.com/pages/11-getting-started.html#programming-in-python>`_.
You may want to read `10 reasons Python rocks for research`_ for a good
description of the benefits of Python compared to MATLAB.

Berkeley teaches its new data science courses using Python.

Python has several versions.  The current version of Python at the time of
writing was version 3.5.  Python versions 3.0 and greater (such as 3.5) differ
in significant ways from earlier versions, such as version 2.7.  Many people
still use Python 2.7, but because the versions are not fully compatible, we
have standardized on Python 3.

*********
Why Atom?
*********

We're going to press you pretty hard to use the Atom text editor.

:doc:`choosing_editor` is a personal decision, and one we recommend you invest
some time in.  For example, your instructors, outside the class, usually use
vim_.

But, for the class, we will be using Atom, and we strongly suggest you do the
same.  This is for several reasons.  Atom:

* is a high-quality open-source text editor with good installers
  available for Windows, OSX and Linux;
* doesn't need a lot of configuration to get started;
* can be configured to work in a very similar to way to other text editors you
  may be used to, such as vim (vim-mode_; ex-mode_) and emacs (emacs-mode_);
* can be used to run code interactively, with the `hydrogen`_ plugin.

.. include:: links_names.inc
