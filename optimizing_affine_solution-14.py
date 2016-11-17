#: check numpy agrees with our negative correlation calculation
x = np.random.normal(size=(100,))
y = np.random.normal(size=(100,))
assert np.allclose(correl_mismatch(x, y), -np.corrcoef(x, y)[0, 1])
