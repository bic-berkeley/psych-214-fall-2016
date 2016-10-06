#- Confirm tranpose of U is inverse of U
np.allclose(np.eye(2), U.T.dot(U))
# True
