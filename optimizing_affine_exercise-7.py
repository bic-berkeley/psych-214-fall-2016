#: the MNI template - also skull stripped
template_img = nib.load('mni_icbm152_t1_tal_nlin_asym_09a_masked_222.nii')
template_data = template_img.get_data()
template_data.shape
# (99, 117, 95)
