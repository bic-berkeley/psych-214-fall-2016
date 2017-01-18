####################################
Exploring cross-subject registration
####################################

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

********************
Reading and homework
********************

Working on projects.
