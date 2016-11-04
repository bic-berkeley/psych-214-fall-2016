data = nib.load('ds114_sub009_t2r1.nii').get_data()
data = data[..., 4:]
data.shape
# (64, 64, 30, 169)
n = data.shape[-1]
