# order=1 for linear interpolation
K = affine_transform(J, M, translation, order=1)
K.shape
# (64, 64, 35)
