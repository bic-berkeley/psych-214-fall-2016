###################
Python coding style
###################

As you become more experienced in coding in general and Python coding in
particular, you will find that your code improves in various ways if you use a
consistent coding style.

*********************
Code style guidelines
*********************

Using a consistent style makes your code easier to read.  Once you have
learned the guidelines, you will spend less time thinking about formatting and
more time thinking about the algorithm and code structure.

* https://www.python.org/dev/peps/pep-0008/
* https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style

The first link above is the official "Style Guide for Python Code", usually
referred to as PEP8_. PEP is an acronym for Python Enhancement Proposal.
There are a couple of potentially helpful tools for helping you conform to the
standard. The `pep8 <https://pypi.python.org/pypi/pep8>`__ package that
provides a commandline tool to check your code against some of the PEP8
standard conventions. Similarly, `autopep8
<https://pypi.python.org/pypi/autopep8>`__ provides a tool to automatically
format your code so that it conforms to the PEP8 standards.

.. _documentation-guidelines:

************************
Documentation guidelines
************************

You will also want to document your code in a consistent way, so you and
others can see at a glance how the code works.  You should write the
documentation as you write the code, to help you think about what the code
should do, and to find the cleanest code design.

The most basic form of documentation is to write :doc:`docstrings` for your
functions, classes and modules.  Good docstrings make your code much easier to
use and understand.

Nearly all scientific Python projects use the `numpy docstring standard`_.
This is a well-defined set of rules for writing a standard docstring, that
makes the docstring easier to read, and later, allows the docstring to be
parsed by automatic tools that can make nice online document like `this
<numpy.ndarray_>`_.

You'll see that the example code that we give you often uses this style, even
for short snippets of code.
