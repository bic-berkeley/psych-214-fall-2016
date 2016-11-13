#- Reslice mean functional to structural voxel space
M, T = nib.affines.to_matvec(struct_vox2mean_vox)
mean_in_struct_space = affine_transform(mean_vol, M, T, structural_data.shape, order=1)
