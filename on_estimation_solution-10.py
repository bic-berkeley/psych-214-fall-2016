#- Residuals orthogonal to design
X.T.dot(residuals) # doctest: +SKIP
# array([-0., -0.])
np.allclose(X.T.dot(residuals), 0)
# True
