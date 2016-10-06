#- Read lines from file and convert to list of floats
pixel_values = []
fobj = open('camera.txt', 'r')
for line in fobj:
    pixel_values.append(float(line))
