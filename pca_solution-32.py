#- Transpose C
#- Reshape the first dimension of C to have the 3D shape of the
#- original data volumes.
C_vols = C.T.reshape(img.shape)
