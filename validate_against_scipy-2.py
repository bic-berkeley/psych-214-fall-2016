# Make random number generation predictable
np.random.seed(1966)
# Make a fake regressor and data.
n = 20
x = np.random.normal(10, 2, size=n)
y = np.random.normal(20, 1, size=n)
plt.plot(x, y, '+')
# [...]
