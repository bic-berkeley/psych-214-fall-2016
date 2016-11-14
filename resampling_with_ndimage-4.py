import nibabel as nib
img = nib.load('ds107_sub012_t1r2.nii')
data = img.get_data()
I = data[..., 0]  # I is the first volume
