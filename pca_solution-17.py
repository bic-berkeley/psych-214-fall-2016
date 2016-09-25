#- Confirm orthogonality of columns in U
np.allclose(U[:, 0].dot(U[:, 1]), 0)
# True
