transformed = affine.transform(moving_data)
regtools.overlay_slices(template_data, transformed, None, 0,
                        "Template", "Transformed")
# <...>
regtools.overlay_slices(template_data, transformed, None, 1,
                        "Template", "Transformed")
# <...>
regtools.overlay_slices(template_data, transformed, None, 2,
                        "Template", "Transformed")
# <...>
