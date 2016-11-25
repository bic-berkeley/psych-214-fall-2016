#: load the fixed "f" image to get parameters
img = nib.load('fds114_sub009_t2r1.nii')
num_slices = img.shape[2]
num_slices
# 30
