######################################################
Sometimes, the NIfTI image stores the TR in the header
######################################################

.. nbplot::

    >>> import numpy as np
    >>> # print arrays to 4 decimal places
    >>> np.set_printoptions(precision=4, suppress=True)
    >>> import nibabel as nib

The `NIfTI1 standard`_ suggests putting the TR of a functional image, into the
voxel dimension field of the header.

You can get the voxel (plus TR) dimensions with the ``get_zooms`` method of
the header object:

.. nbplot::

    >>> func_img = nib.load('ds114_sub009_t2r1.nii')
    >>> header = func_img.header
    >>> header.get_zooms()
    (4.0, 4.0, 4.0000162, 2.5)

In this case, the image spatial voxel sizes are (4 by 4 by 4)
millimeters, and the TR is 2.5 seconds.

In fact these values come from the NIfTI header field called ``pixdim``:

.. nbplot::

    >>> print(header)
    <class 'nibabel.nifti1.Nifti1Header'> object, endian='<'
    sizeof_hdr      : 348
    data_type       : b''
    db_name         : b'?TR:2500.000 TE:50'
    extents         : 0
    session_error   : 0
    regular         : b'r'
    dim_info        : 0
    dim             : [  4  64  64  30 173   1   1   1]
    intent_p1       : 0.0
    intent_p2       : 0.0
    intent_p3       : 0.0
    intent_code     : none
    datatype        : int16
    bitpix          : 16
    slice_start     : 0
    pixdim          : [-1.   4.   4.   4.   2.5  1.   1.   1. ]
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
    glmax           : 255
    glmin           : 0
    descrip         : b''
    aux_file        : b''
    qform_code      : scanner
    sform_code      : scanner
    quatern_b       : 0.0
    quatern_c       : 0.9958999752998352
    quatern_d       : -0.090460866689682
    qoffset_x       : 124.24400329589844
    qoffset_y       : -103.4496841430664
    qoffset_z       : -33.49285888671875
    srow_x          : [  -4.       0.       0.     124.244]
    srow_y          : [   0.        3.9345    0.7207 -103.4497]
    srow_z          : [  0.      -0.7207   3.9346 -33.4929]
    intent_name     : b''
    magic           : b'n+1'

Unfortunately, it is common for people writing NIfTI images not to write this
information correctly into the header, so we have to be careful, and very
suspicious, if the TR value appears to be 0 or 1.
