#######################################
Making and saving new images in nibabel
#######################################

We often want to do some processing on an image, then save the processed image
back to an image file on disk.

When we load an image from disk, we get back an image object. When we load a
NIfTI ``.nii`` image, we get an image object of type ``Nifti1Image``.

.. nbplot::

    >>> import numpy as np

.. nbplot::

    >>> import nibabel as nib
    >>> img = nib.load('ds114_sub009_highres.nii')
    >>> type(img)
    <class 'nibabel.nifti1.Nifti1Image'>

Maybe we were worried about some very high values in the image, and we wanted
to clip them down to a more reasonable number:

.. nbplot::

    >>> data = img.get_data()
    >>> data.max()
    memmap(3237.0, dtype=float32)

We might consider clipping the top 5 percent of voxel values:

.. nbplot::

    >>> data = img.get_data()
    >>> top_95_thresh = np.percentile(data, 95)
    >>> top_95_thresh
    722.0

.. nbplot::

    >>> new_data = data.copy()
    >>> new_data[new_data > top_95_thresh] = top_95_thresh
    >>> new_data.max()
    memmap(722.0, dtype=float32)

We can make a new ``Nifti1Image`` by constructing it directly.  We pass the
new data, the image affine, and (optionally) a template :doc:`header
<image_header_and_affine>` for the image:

.. nbplot::

    >>> clipped_img = nib.Nifti1Image(new_data, img.affine, img.header)
    >>> type(clipped_img)
    <class 'nibabel.nifti1.Nifti1Image'>

The ``nib.Nifti1Image`` call copies and adapts the passed header to the new
image data shape, and affine.

.. nbplot::

    >>> # Show the original data array shape from the original header
    >>> img.header.get_data_shape()
    (256, 156, 256)

.. nbplot::

    >>> # Here we construct a new empty header
    >>> empty_header = nib.Nifti1Header()
    >>> empty_header.get_data_shape()
    (0,)

If we make a new image with this header, the constructor routine fixes the
header to have the correct shape for the data array:

.. nbplot::

    >>> another_img = nib.Nifti1Image(new_data, img.affine, empty_header)
    >>> another_img.header.get_data_shape()
    (256, 156, 256)

We can save the new image with ``nib.save``:

.. nbplot::

    >>> nib.save(clipped_img, 'clipped_image.nii')

This image has the clipped data:

.. nbplot::

    >>> nib.load('clipped_image.nii').get_data().max()
    memmap(722.0, dtype=float32)
