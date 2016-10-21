img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
data = data[..., 4:]
