# Plot the neural prediction against the data
neural = neural[1:]
# Notice the 'o' to specify the "line marker"
plt.plot(neural, voxel_time_course, 'o')
# [...]
# Set the axis limits to give space on left and right
axis = plt.gca()
axis.set_xlim(-0.1, 1.1)
# (...)
