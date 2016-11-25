#: save new copy of image with first four volumes dropped
img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
fixed = nib.Nifti1Image(data[..., 4:], img.affine, img.header)
nib.save(fixed, 'fds114_sub009_t2r1.nii')
