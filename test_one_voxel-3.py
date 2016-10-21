convolved = np.loadtxt('ds114_sub009_t2r1_conv.txt')
# Knock off first 4 elements to match data
convolved = convolved[4:]
N = len(convolved)
X = np.ones((N, 2))
X[:, 0] = convolved
plt.imshow(X, interpolation='nearest', cmap='gray', aspect=0.1)
# <...>
