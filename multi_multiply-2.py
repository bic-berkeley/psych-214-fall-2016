X = np.ones((12, 2))
X[:, 0] = np.linspace(-1, 1, 12)
plt.imshow(X, interpolation='nearest', cmap='gray')
# <...>
