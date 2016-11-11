""" First go at brain activation exercise
"""

#: import common modules
import numpy as np  # the Python array package
import matplotlib.pyplot as plt  # the Python plotting package
# Display array values to 6 digits of precision
np.set_printoptions(precision=4, suppress=True)

#- Read the file into an array called "task".
#- "task" should have 3 columns (onset, duration, amplitude)
#- HINT: np.loadtxt

#- Select first two columns and divide by TR

#- Load the image and check the image shape to get the number of TRs

#- Make new zero vector

#: try running this if you don't believe me
len(range(4, 16))

#- Fill in values of 1 for positions of on blocks in time course

#- Plot the time course

#- Make two boolean arrays encoding task, rest


#- Create a new 4D array only containing the task volumes

#- Create a new 4D array only containing the rest volumes

#- Create the mean volume across all the task volumes.
#- Then create the mean volume across all the rest volumes

#- Create a difference volume

#- Show a slice over the third dimension

#- Calculate the SD across voxels for each volume
#- Identify the outlier volume

#- Use slicing to remove outlier volume from rest volumes

#- Make new mean for rest volumes, subtract from task mean

#- show same slice from old and new difference volume
