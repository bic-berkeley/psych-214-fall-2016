# This is slicing over all three of the space axes
voxel_time_course = data[42, 32, 19]
voxel_time_course.shape
# (172,)
plt.plot(voxel_time_course)
# [...]
