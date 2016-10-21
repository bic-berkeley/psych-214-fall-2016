#- Correlation of predicted neural time course with voxel signal time
#- course
np.corrcoef(neural_prediction_no_0, voxel_values)
# array([[ 1.    ,  0.3117],
# [ 0.3117,  1.    ]])
