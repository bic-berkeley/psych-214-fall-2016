#: load the template image we will resample from
template_img = nib.load('mni_icbm152_t1_tal_nlin_asym_09a.nii')
template_data = template_img.get_data()
template_data.shape
# (197, 233, 189)
