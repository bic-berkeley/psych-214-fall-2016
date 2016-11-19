#: load y_ds107_sub012_highres.nii with nibabel
# get the image array data
deformations_img = nib.load('y_ds107_sub012_highres.nii')
deformations_data = deformations_img.get_data()
deformations_data.shape
# (121, 145, 121, 1, 3)
