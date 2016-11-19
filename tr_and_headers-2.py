func_img = nib.load('ds114_sub009_t2r1.nii')
header = func_img.header
header.get_zooms()
# (4.0, 4.0, 4.0000162, 2.5)
