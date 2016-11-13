#: the resulting rotated image
rotated_img = nib.load('rotated_volume.nii')
rotated_vol0 = rotated_img.get_data()
rotated_vol0.shape
# (64, 64, 35)
