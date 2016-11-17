#: ds114 subject 9 highres, skull stripped
subject_img = nib.load('ds114_sub009_highres_brain_222.nii')
subject_data = subject_img.get_data()
subject_data.shape
# (88, 78, 128)
