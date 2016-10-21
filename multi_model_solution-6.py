#- Reshape the 4D data to voxel by time 2D
#- Transpose to give time by voxel 2D
#- Calculate the pseudoinverse of the design
#- Apply to time by voxel array to get betas
data_2d = np.reshape(data, (-1, data.shape[-1]))
betas = npl.pinv(design).dot(data_2d.T)
betas.shape
# (2, 122880)
