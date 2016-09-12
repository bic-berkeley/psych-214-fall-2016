#- Try reshaping using some candidate pairs
pixel_array = np.array(pixel_values)
try1 = np.reshape(pixel_array, (130, 204, 32))
plt.imshow(try1[:, :, 15])  # A middle slice in the third dimension
# <...>
