# Correlate the neural time course with the voxel time course
np.corrcoef(neural, voxel_time_course)
# array([[ 1.    ,  0.5429],
# [ 0.5429,  1.    ]])
