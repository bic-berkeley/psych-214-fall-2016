import numpy.linalg as npl
Xp = npl.pinv(X)
beta_hat = Xp.dot(voxel_time_course)
beta_hat
# array([   31.1855,  2029.3677])
