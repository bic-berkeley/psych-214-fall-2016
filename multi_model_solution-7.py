#- Transpose betas to give voxels by 2 array
#- Reshape into 4D array, with same 3D shape as original data,
#- last dimension length 2
betas_4d = np.reshape(betas.T, img.shape[:-1] + (-1,))
