#- Read file into list of float values
pixel_values = []
for line in open('anatomical.txt', 'r'):
    pixel_values.append(float(line))
