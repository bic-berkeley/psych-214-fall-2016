#: the first volume of ds107_sub012_t1r2.nii
img_4d = nib.load('ds107_sub012_t1r2.nii')
data = img_4d.get_data()
vol0 = data[..., 0]
