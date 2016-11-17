#: check the cost function returns the previous value if params
# say to do no transformation
current = correl_mismatch(subject_resampled, template_data)
redone = cost_function([0, 0, 0, 0, 0, 0, 1, 1, 1])
assert np.allclose(current, redone)
