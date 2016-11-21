##################
Anterior cingulate
##################

See: :cite:`vogt1995human`.

Most brain hemispheres (65%) have a single *cingulate sulcus* delimited by a
*cingulate sulcus* above it:

.. image:: images/vogt_1995_single_cs.png

The rest have two cingulate sulci, with an extra *superior cingulate sulcus*
and *superior cingulate gyrus*:

.. image:: images/vogt_1995_alternatives.png

The cytoarchitectonic regions appear to correspond to the sulcal anatomy:

.. image:: images/vogt_1995_cytoarchitecture.png

******************************************
Match brain to template in high resolution
******************************************

We are going to run the dipy non-linear registration to match a
high-resolution structural image to a high-resolution version of the template.

Then we're going to see what kind of job this does of matching anterior
cingulate anatomy to the template.

* make sure you have these files in your working directory:

  * :download:`ds114_sub009_highres.nii`;
  * :download:`ds114_sub009_highres_brain_mask.nii`;
  * :download:`mni_icbm152_t1_tal_nlin_asym_09a.nii`;
  * :download:`mni_icbm152_t1_tal_nlin_asym_09a_mask.nii`;
  * :download:`ds114_sub009_highres_brain_mask.nii`;
  * :download:`dipy_registration.py`;

* have a look at ``dipy_registration.py`` for useful functions;

* open IPython and::

  .. ipython::

     In [1]: run dipy_registration.py
     In [2]: mapping = register_save('mni_icbm152_t1_tal_nlin_asym_09a.nii',
     ...:                            'mni_icbm152_t1_tal_nlin_asym_09a_mask.nii',
     ...:                            'ds114_sub009_highres.nii',
     ...:                            'ds114_sub009_highres_brain_mask.nii')

* leave that running - it will take something like 10-20 minutes depending on
  your machine.  Meanwhile...

*****************
Reviewing anatomy
*****************

We will be using `MRIcron`_:

* `install MRIcron`_;
* review the help on how to `draw with MRIcron`_.
* open :download:`ds114_sub009_highres.nii` with MRIcron.  Scroll around the
  image, and have a look at the controls and menu items;
* what kind of cingulate anatomy (single, double) does this subject have in
  each hemisphere;
* make a new MRIcron window and open ``mni_icbm152_t1_tal_nlin_asym_09a.nii``;
* on a piece of paper, write down what you would like the registration to do
  to the subject's brain:

  * sketch the sulcal anatomy of the medial surface of each hemisphere for the
    subject and the template, as in the Vogt figure above;
  * do the same for the template image;
  * draw arrows from the subject hemisphere to the matching part of the
    template;

* in MRIcron, use the "View" menu to go to the coronal sections of the
  individual subject brain image;
* using the Vogt paper diagram, draw your estimate for the position for left
  and right area 24 (a, b, c combined) on three or four adjacent slices
  through the anterior cingulate.  Be careful: watch the y slice index at the
  top left to make sure you are moving one slice at a time; have a look at the
  VOI display to make sure it looks OK before saving;
* using the "Draw" menu in MRICron; "Save VOI" to save this definition in
  MRIcron's own format.  Add something like ``_area_24`` to the VOI name when
  saving;
* using the Draw menu "Convert" item, convert the VOI to a NIfTI file;
* if the registration has finished, open the new
  ``w_ds114_sub002_highres.nii`` file in MRIcron.  Compare it to the template,
  visually.  What do you think of the match?  How does it correspond to your
  drawing?
* try loading the template image, and using the warped individual brain as an
  overlay.  Play with the overlay settings to get an idea of the quality of
  the registration;
* investigate the ``dipy_registration.py`` code for a useful function to
  resample the region definition file to the template voxel space.  Apply this
  function (or your own, if you prefer) to your region definition, to write
  out a version of the region image in template space;
* use the "Overlay" menu to load the resampled region on the:

  * template image;
  * resampled (warped) individual image;

  What do you think of the registration?  Do you think the cytoarchitecture
  lines up?
