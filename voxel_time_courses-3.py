# Drop the first volume
data = img.get_data()
data = data[..., 1:]
data.shape
# (64, 64, 30, 172)
