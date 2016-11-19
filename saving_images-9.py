another_img = nib.Nifti1Image(new_data, img.affine, empty_header)
another_img.header.get_data_shape()
# (256, 156, 256)
