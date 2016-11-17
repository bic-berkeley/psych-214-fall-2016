coords_last = in_vox_coords.transpose(1, 2, 3, 0)
mean_vox_coords = nib.affines.apply_affine(struct_vox2mean_vox,
                                           coords_last)
coords_first_again = mean_vox_coords.transpose(3, 0, 1, 2)
