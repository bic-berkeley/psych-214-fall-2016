y_hat = X.dot(beta_hat)
e_vec = voxel_time_course - y_hat
print(np.sum(e_vec ** 2))
# 41405.57...
plt.plot(voxel_time_course)
# [...]
plt.plot(y_hat)
# [...]
