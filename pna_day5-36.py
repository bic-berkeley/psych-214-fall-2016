import nibabel as nib
img = nib.load('ds114_sub009_t2r1.nii', mmap=False)
data = img.get_data()
data.shape
