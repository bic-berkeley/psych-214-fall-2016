bold_img = nib.load('ds114_sub009_t2r1.nii')
mean_bold_data = bold_img.get_data().mean(axis=-1)
structural_img = nib.load('ds114_sub009_highres.nii')
structural_data = structural_img.get_data()
