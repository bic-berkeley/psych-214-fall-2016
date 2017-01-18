###########################
The image header and affine
###########################

See: `coordinate systems and affine transforms`_ for an introduction.

.. nbplot::
    :include-source: false

    >>> # compatibility with Python 2
    >>> from __future__ import print_function
    >>> from __future__ import division

.. nbplot::

    >>> # import common modules
    >>> import numpy as np
    >>> np.set_printoptions(precision=4, suppress=True)  # print arrays to 4DP
    >>> import matplotlib.pyplot as plt

.. nbplot::

    >>> #: gray colormap and nearest neighbor interpolation by default
    >>> plt.rcParams['image.cmap'] = 'gray'
    >>> plt.rcParams['image.interpolation'] = 'nearest'

****************
The image affine
****************

So far we have not paid much attention to the image *header*.  We first saw
the image header in :doc:`classwork/day_00/what_is_an_image`.

From that exploration, we found that image consists of:

* the array data;
* metadata (data about the array data).

The header contains the metadata for the image.

One piece of metadata, is the image affine.  You can download the anatomical
image below from :download:`ds107_sub012_highres.nii`:

.. nbplot::

    >>> import nibabel as nib
    >>> img = nib.load('ds107_sub012_highres.nii')
    >>> img.affine
    array([[   1.    ,    0.    ,    0.    , -127.    ],
           [   0.    ,    1.    ,    0.    ,  -83.3253],
           [   0.    ,    0.    ,    1.    ,  -90.0533],
           [   0.    ,    0.    ,    0.    ,    1.    ]])

As you can imagine, nibabel is getting the affine from the header:

.. nbplot::

    >>> print(img.header)
    <class 'nibabel.nifti1.Nifti1Header'> object, endian='<'
    sizeof_hdr      : 348
    data_type       : b''
    db_name         : b''
    extents         : 0
    session_error   : 0
    regular         : b'r'
    dim_info        : 0
    dim             : [  3 256 208 192   1   1   1   1]
    intent_p1       : 0.0
    intent_p2       : 0.0
    intent_p3       : 0.0
    intent_code     : none
    datatype        : int16
    bitpix          : 16
    slice_start     : 0
    pixdim          : [ 1.  1.  1.  1.  0.  0.  0.  0.]
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
    descrip         : b'FSL4.0'
    aux_file        : b''
    qform_code      : scanner
    sform_code      : scanner
    quatern_b       : 0.0
    quatern_c       : 0.0
    quatern_d       : 0.0
    qoffset_x       : -127.0
    qoffset_y       : -83.32530212402344
    qoffset_z       : -90.05328369140625
    srow_x          : [   1.    0.    0. -127.]
    srow_y          : [  0.       1.       0.     -83.3253]
    srow_z          : [  0.       0.       1.     -90.0533]
    intent_name     : b''
    magic           : b'n+1'

Notice the ``srow_x, srow_y, srow_z`` fields in the header, that contain the
affine for this image. It is not always this simple though |--| see
http://nifti.nimh.nih.gov/nifti-1 for more details. In general, nibabel will
take care of this for you, by extracting the affine from the header, and
returning it via ``img.affine``.

*********************************************
Nifti images can also be ``.img, .hdr`` pairs
*********************************************

So far, all the images we have seen have been NIfTI format images, stored in a
single file with a ``.nii`` extension. The single file contains the header
information, and the image array data.

The NIfTI format also allows the image to be stored as two files, one with
extension ``.img`` storing the image array data, and another with extension
``.hdr`` storing the header. These are called *NIfTI pair* images.

For example, consider this pair of files |--|
:download:`ds114_sub009_highres_moved.img` and
:download:`ds114_sub009_highres_moved.hdr`. These two files together form one
NIfTI image. You can load these with nibabel in the usual way:

.. nbplot::

    >>> pair_img = nib.load('ds114_sub009_highres_moved.img')
    >>> pair_img.affine
    array([[   0.9416,   -0.4311,   -0.0586,  -98.8336],
           [   0.336 ,    1.1887,    0.2264, -164.1377],
           [  -0.0215,   -0.3028,    0.9723, -158.4178],
           [   0.    ,    0.    ,    0.    ,    1.    ]])

This form of the NIfTI image is getting less common, because it is
inconvenient to have to keep the ``.img`` and ``.hdr`` files together, but you
may still find them used. They have only one advantage, which is that, if some
software wants to change only the header information, it only has to rewrite a
small ``.hdr`` file, rather than the whole ``.nii`` file containing the image
data and the header.
