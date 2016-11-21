transform = AffineTransform3D()
# Bump up the iterations to get an more exact fit
affreg.level_iters = [1000, 1000, 100]
affine = affreg.optimize(template_data, moving_data, transform, params0,
                         template_affine, moving_affine,
                         starting_affine=rigid.affine)
# Optimizing level 2 [max iter: 1000]
# Optimizing level 1 [max iter: 1000]
# Optimizing level 0 [max iter: 100]
