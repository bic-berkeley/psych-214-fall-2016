#: load the subject data that we will resample from
subject_img = nib.load('ds107_sub012_highres.nii')
subject_data = subject_img.get_data()
subject_data.shape
# (256, 208, 192)
