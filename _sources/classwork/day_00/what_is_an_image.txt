#################
What is an image?
#################

In this exercise we explore the nature of NIfTI images.

The Python commands here are written with a ``>>>`` prefix.  The ``>>>`` is
the prompt in the Python interactive console.  This is the prompt you get if
you type ``python3`` at the shell prompt.  We suggest that you use the
IPython_ console instead of the Python console to type your commands.  Get
the IPython terminal by installing IPython with pip_, then typing ``ipython``.

First we will have a look at Python strings. Here is a variable called
``my_string`` with value "PNA is hard but fair"

.. testsetup::

    import os
    import sys
    os.chdir('classwork/day_00')

.. nbplot::

    >>> my_string = "neuroimaging is hard but fair"

We can see what type of thing this variable contains (points to) using
the ``type`` function:

.. nbplot::

    >>> type(my_string)
    <... 'str'>

We can see how many characters the string has with the ``len`` function:

.. nbplot::

    >>> len(my_string)
    29

.. nbplot::

    >>> # The first character of the string
    >>> print(my_string[0])
    n

.. nbplot::

    >>> # The last character of the string (don't forget indexing starts at 0)
    >>> print(my_string[28])
    r

Now we introduce string *slicing*. This is where you take some sequential
characters from the string, using the colon (``:``) between the square
brackets. The value before the colon is the index to the first character you
want, and the value after the colon is the index to the character *after* the
last character you want. It sounds strange, but you will get used to it...

.. nbplot::

    >>> # The first two characters of the string
    >>> print(my_string[0:2])  # from index 0 up to, but not including, 2
    ne

.. nbplot::

    >>> # The first 5 characters of the string
    >>> print(my_string[0:5])  # from index 0 up to, but not including, 5
    neuro

We will go into more details on strings and slicing soon.

Now we will try loading an example image and seeing if we can understand
the image data.

.. nbplot::

    >>> # This is a Python module
    >>> import os  # module for interacting with the operating system

If you want to explore modules or objects, type their name followed by a
period, and press tab to see what functions or classes are available.

Try this now.  Type `os.` (`os.` followed by a period) then press tab, to see
what functions are in the ``os`` module. Continue typing so you have
``os.getcwd``, and then type ``?`` followed by Return. This shows you
the help for the ``os.getcwd`` function.

The image we are going to explore is in the same directory as this exercise.

.. nbplot::

    >>> # Get the current working directory (CWD)
    >>> cwd = os.getcwd()
    >>> print(cwd)  # doctest: +SKIP
    /Users/myuser/for-class

.. nbplot::

    >>> # List files and directories in the current working directory
    >>> print(os.listdir(cwd))
    [...]

Let's read the image into memory.

.. nbplot::

    >>> # Open a file in Read Binary mode
    >>> fobj = open('ds114_sub009_highres.nii', 'rb')
    >>> print(fobj)
    <...>

.. nbplot::

    >>> # read all the characters into a variable in memory
    >>> contents = fobj.read()

How do I find out what ``type`` of object is attached to this variable
called ``contents``?

.. nbplot::

    >>> # your code here

How big is this file in terms of bytes? Can you find out from the
``contents`` variable? (Hint: you want to know the length of
``contents``).

.. nbplot::

    >>> # n_bytes = ?

.. nbplot::
    :include-source: false

    >>> n_bytes = len(contents)

If 1 mebibyte (MiB) (http://en.wikipedia.org/wiki/Megabyte) is size 1024 \*
1024, what is the file size in MiB? (Hint - the right answer is between 0 and
100).

.. nbplot::

    >>> # n_mib = ?

.. nbplot::
    :include-source: false

    >>> n_mib = n_bytes / (1024 * 1024)

This is a `NIfTI1 format <http://nifti.nimh.nih.gov/nifti-1>`__ file.
That means that the first 352 bytes contains the "header" that describes
the parameters of the image and the data following.

We want to print out the contents of the first 352 bytes of ``contents``
to have a look at it.

To do this, we are going to need string slicing to get the first 352
bytes:

.. nbplot::

    >>> # Here you print out the first 352 characters of `contents`

.. nbplot::
    :include-source: false

    >>> print(contents[:352])  # doctest: +SKIP

Which software wrote this image?

Here is the format of the NIfTI1 header :
http://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields

We are now going to try and work out the ``datatype`` of this image.  This is
stored in the ``datatype`` field of the header. Careful - there is also a
``data_type`` field (with an underscore), which we will ignore.

Looking at the web page above, how many bytes is the ``datatype`` value
stored in?

How would you get the bytes in ``contents`` that contain the ``datatype``
value? (Hint - you need slicing again, and the information from ``Byte
offset`` column in the NIfTI1 header page above):

.. nbplot::

    >>> # data_type_chars = ?

.. nbplot::
    :include-source: false

    >>> data_type_chars = contents[70:72]

The ``datatype`` value is stored in binary form (rather than text form).
The value for ``datatype`` is stored in the header in the same format
that the computer stores the number in memory. We want to convert this
binary format to a number that Python understands. To do that, we use
the `struct module <https://docs.python.org/2/library/struct.html>`__.

.. nbplot::

    >>> import struct

We are going to use the ``struct.unpack`` function. Open a new cell
below this one with ``b`` and type ``struct.unpack?`` followed by
Shift-Return to see the help for this function.

Now we have read the help, we know we need two things. The first is a
string that give the code for the binary format of the data. This is the
"format string". The second is the string containing the bytes of the
data.

We first need to specify the format of the character data. Have a look
at the `help on format
strings <https://docs.python.org/2/library/struct.html#format-characters>`__
in the Python documentation and the NIfTI web page above.

Here is the format specifier for our value:

.. nbplot::

    >>> fmt_specifier = 'h'  # Why? (check the web pages above)

Now we read the datatype value into a number that Python understands:

.. nbplot::

    >>> datatype = struct.unpack(fmt_specifier, data_type_chars)
    >>> print(datatype)
    (16,)

This is a numerical *code* for a data type. What actual data type is this?
(See:
http://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields/nifti1fields\_pages/datatype.html)

We could continue reading the NIfTI header in the same way, but luckily
someone has done that work for us. Enter the ``nibabel`` package:

.. nbplot::

    >>> import nibabel

For now, we will use this package without worrying much about how it works.
Have a look to see what ``nibabel`` can do by opening up a new cell with ``b``
and typing ``nibabel?`` and ``nibabel.`` followed by Tab.

As with most Python packages, you can check what version of nibabel you have
by printing the ``__version__`` variable of the package:

.. nbplot::

    >>> print(nibabel.__version__)  # doctest: +SKIP
    2.1.0

If you have a nibabel version below 2.0.0, please let your instructor know so
they can fix that.

You can load an image into memory like this:

.. nbplot::

    >>> img = nibabel.load('ds114_sub009_highres.nii')

Let's have a look at the header:

.. nbplot::

    >>> print(img.header)  # doctest: +SKIP
    <class 'nibabel.nifti1.Nifti1Header'> object, endian='<'
    sizeof_hdr      : 348
    data_type       :
    db_name         :
    extents         : 0
    session_error   : 0
    regular         : r
    dim_info        : 0
    dim             : [  3 256 156 256   1   1   1   1]
    intent_p1       : 0.0
    intent_p2       : 0.0
    intent_p3       : 0.0
    intent_code     : none
    datatype        : float32
    bitpix          : 32
    slice_start     : 0
    pixdim          : [ 1.          1.          1.30022228  1.          0.00972     0.          0.
      0.        ]
    vox_offset      : 0.0
    scl_slope       : nan
    scl_inter       : nan
    slice_end       : 0
    slice_code      : unknown
    xyzt_units      : 10
    cal_max         : 0.0
    cal_min         : 0.0
    slice_duration  : 0.0
    toffset         : 0.0
    glmax           : 0
    glmin           : 0
    descrip         : FSL5.0
    aux_file        :
    qform_code      : scanner
    sform_code      : scanner
    quatern_b       : -0.117474533617
    quatern_c       : 0.00814610160887
    quatern_d       : 0.0224816054106
    qoffset_x       : -129.82572937
    qoffset_y       : -119.090568542
    qoffset_z       : -143.417770386
    srow_x          : [  9.98856485e-01  -6.05286658e-02   1.08951973e-02  -1.29825729e+02]
    srow_y          : [  4.27253172e-02   1.26302111e+00   2.33620942e-01  -1.19090569e+02]
    srow_z          : [ -2.14542095e-02  -3.02806526e-01   9.72266734e-01  -1.43417770e+02]
    intent_name     :
    magic           : n+1

As you can see, it has worked out the datatype for us.

Soon, we do some more work to get used to basic Python.  After that we will
start playing with the image using the Python tools for arrays, and for
plotting.

.. testcleanup::

    os.chdir('../..')
