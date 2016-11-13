#: a quick check the cost function returns the current value without rotations
current = correl_mismatch(vol0, rotated_vol0)
redone = cost_function([0, 0, 0])
assert np.allclose(current, redone)
