transform = RigidTransform3D()
rigid = affreg.optimize(template_data, moving_data, transform, params0,
                        template_affine, moving_affine,
                        starting_affine=translation.affine)
# Optimizing level 2 [max iter: 10]
# Optimizing level 1 [max iter: 10]
# Optimizing level 0 [max iter: 5]
