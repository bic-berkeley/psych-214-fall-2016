#- Check you get the same answer when selecting a voxel time course
#- and running the correlation on that time course.  One example voxel
#- could be the voxel at array coordinate [42, 32, 19]
voxel_time_course = data[42, 32, 19]
single_cc = np.corrcoef(voxel_time_course, time_course)[0, 1]
assert np.allclose(correlations[42, 32, 19], single_cc)
