##########################
Cross-subject registration
##########################

*********
Logistics
*********

* problems from projects;

********
Teaching
********

* :doc:`saving_images`;
* SPM coregistration:

  * copy the structural::

      cp ds107_sub012_highres.nii a_structural.nii

  * create the mean of the functional image::

    >>> import nibabel as nib
    >>> img = nib.load('ds107_sub012_t1r2.nii')
    >>> mean_vol = img.get_data().mean(axis=-1)
    >>> mean_img = nib.Nifti1Image(mean_vol, img.affine, img.header)
    >>> nib.save(mean_img, 'mean_functional.nii')

  * run coregistration in SPM.

* running cross-subject normalizations in SPM;
* making a distortion field in SPM;
* applying the SPM distortion field;

    * :doc:`numpy_squeeze`;
    * :doc:`numpy_transpose`;
    * :doc:`numpy_meshgrid`;
    * :doc:`map_coordinates`;
    * :doc:`applying_deformations_exercise`.

********************
Reading and homework
********************

Working on projects.
