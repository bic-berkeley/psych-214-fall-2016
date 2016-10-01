N = len(convolved)
X = np.ones((N, 2))
X[:, 0] = convolved
plt.imshow(X, interpolation='nearest', cmap='gray', aspect=0.1)
# <...>
