x = np.arange(0, np.pi * 2, 0.1)
fig, axes = plt.subplots(2, 1)
axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))
# [...]
