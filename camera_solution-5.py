#- Convert list to array and reshape
pixel_array = np.array(pixel_values)
# The shape values shoule be integers
pixel_array = np.reshape(pixel_array, (int(M), int(N)))
pixel_array.shape
# (512, 512)
