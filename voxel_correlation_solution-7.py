#- Drop the first 4 volumes, and the first 4 on-off values.
data = img.get_data()
data = data[..., 4:]
time_course = time_course[4:]
