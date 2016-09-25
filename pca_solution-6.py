#- Slice the image data array to give array with only first two
#- volumes
first_two = data[..., :2]
first_two.shape
# (64, 64, 30, 2)
