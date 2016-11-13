#- Use affine_transform and the tranformation components to resample
#- structural to functional
struct_in_mean_space = affine_transform(structural_data, M, T, mean_vol.shape, order=1)
struct_in_mean_space.shape
# (64, 64, 30)
