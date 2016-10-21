#- Correlation of the convolved time course with voxel time course
np.corrcoef(hemodynamic_prediction, voxel_values)
# array([[ 1.    ,  0.3586],
# [ 0.3586,  1.    ]])
