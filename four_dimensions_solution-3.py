#- Load image object using nibabel
#- Turn off nibabel memory mapping.
fname = 'ds107_sub012_t1r2.nii'
import nibabel as nib
img = nib.load(fname, mmap=False)
