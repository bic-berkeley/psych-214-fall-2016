#: Load the image data as an array
# Drop the first 4 3D volumes from the array
# (We already saw that these were abnormal)
data = img.get_data()[..., 4:]
