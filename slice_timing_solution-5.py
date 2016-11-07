#: Remove the first volume by slicing
fixed_data = data[..., 1:]
fixed_data.shape
# (64, 64, 30, 172)
