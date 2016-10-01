#- Make new mean for rest volumes, subtract from task mean
off_mean_fixed = off_volumes_fixed.mean(axis=-1)
difference_fixed = on_mean - off_mean_fixed
