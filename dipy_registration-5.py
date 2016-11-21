identity = np.eye(4)
affine_map = AffineMap(identity,
                       template_data.shape, template_affine,
                       moving_data.shape, moving_affine)
resampled = affine_map.transform(moving_data)
regtools.overlay_slices(template_data, resampled, None, 0,
                        "Template", "Moving")
# <...>
regtools.overlay_slices(template_data, resampled, None, 1,
                        "Template", "Moving")
# <...>
regtools.overlay_slices(template_data, resampled, None, 2,
                        "Template", "Moving")
# <...>
