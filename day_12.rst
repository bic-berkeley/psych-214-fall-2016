#######################################
November 28: registration and scripting
#######################################

*************
Presentations
*************

Problems from projects.

********
Teaching
********

Registration
============

* nibabel image viewer:

  .. code-block:: ipython

    In [1]: import nibabel as nib
    In [2]: import matplotlib.pyplot as plt
    In [3]: %matplotlib
    In [4]: structural = nib.load('ds114_sub009_highres.nii')
    In [5]: functional = nib.load('ds114_sub009_t2r1.nii')
    In [6]: func_viewer = functional.orthoview()
    In [7]: struct_viewer = structural.orthoview()
    In [8]: func_viewer.link_to(struct_viewer)

* :doc:`dipy_registration`;
* example registration problem |--| :doc:`anterior_cingulate`.

Scripting
=========

* :doc:`introducing_nipype`;
* :doc:`spm_slice_timing_exercise`;
* the rest of the analysis in SPM:

  * motion correction (registration between first image and later images in
    time series);
  * coregistration (registration between structural and functional);
  * spatial normalization (registration between structural and template);
  * reslicing (resampling images in to space of template);
  * smoothing;

* :doc:`full_scripting`.

********************
Reading and homework
********************

Working on projects.
