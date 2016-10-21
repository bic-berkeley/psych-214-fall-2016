#: subtracting rest from task scans
task_scans = data_no_0[..., neural_prediction_no_0 == 1]
rest_scans = data_no_0[..., neural_prediction_no_0 == 0]
difference = task_scans.mean(axis=-1) - rest_scans.mean(axis=-1)
