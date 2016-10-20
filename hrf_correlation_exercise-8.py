#: subtracting rest from task scans
task_scans = data_no_0[..., neural_prediction_no_0 == 1]
rest_scans = data_no_0[..., neural_prediction_no_0 == 0]
difference = np.mean(task_scans, axis=-1) - np.mean(rest_scans, axis=-1)
