#: remove length-1 4th dimension from deformation data
deformations_data = np.squeeze(deformations_data)
deformations_data.shape
# (121, 145, 121, 3)
