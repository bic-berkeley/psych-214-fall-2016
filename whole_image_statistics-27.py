bonferroni_theta = 0.05 / N
bonferroni_theta
# 2.3143...e-06
plt.imshow(p_3d[:, :, 15] < bonferroni_theta, cmap='gray')
# <...>
