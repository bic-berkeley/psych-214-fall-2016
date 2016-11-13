#: You could try this quick check that 0 rotations give the same
# output back
not_changed = apply_rotations(rotated_vol0, [0, 0, 0])
assert np.allclose(not_changed, rotated_vol0)
