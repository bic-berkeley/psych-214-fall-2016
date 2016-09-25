#- Transpose C
#- Reshape the first dimension of C to have the 3D shape of the
#- original data volumes.
C_vols = C.T.reshape(vol_shape + (2,))
C_vols.shape
# (64, 64, 30, 2)
