#: some checks that the function does the right thing
# Identity params gives identity affine
assert np.allclose(params2affine([0, 0, 0, 0, 0, 0, 1, 1, 1]),
                   np.eye(4))
# Some zooms
assert np.allclose(params2affine([0, 0, 0, 0, 0, 0, 2, 3, 4]),
                   np.diag([2, 3, 4, 1]))
# Some translations
assert np.allclose(params2affine([0, 0, 0, 0, 0, 0, 2, 3, 4]),
                   np.diag([2, 3, 4, 1]))
# Some rotations
assert np.allclose(params2affine([0, 0, 0, 0, 0, 0.2, 1, 1, 1]),
                   [[np.cos(0.2), -np.sin(0.2), 0, 0],
                    [np.sin(0.2), np.cos(0.2), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1],
                    ])
assert np.allclose(params2affine([0, 0, 0, 0, 0, 0.2, 1, 1, 1]),
                   [[np.cos(0.2), -np.sin(0.2), 0, 0],
                    [np.sin(0.2), np.cos(0.2), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1],
                    ])
assert np.allclose(params2affine([0, 0, 0, 0, -0.1, 0, 1, 1, 1]),
                   [[np.cos(-0.1), 0, np.sin(-0.1), 0],
                    [0, 1, 0, 0],
                    [-np.sin(-0.1), 0, np.cos(-0.1), 0],
                    [0, 0, 0, 1],
                    ])
assert np.allclose(params2affine([0, 0, 0, 0.3, 0, 0, 1, 1, 1]),
                   [[1, 0, 0, 0],
                    [0, np.cos(0.3), -np.sin(0.3), 0],
                    [0, np.sin(0.3), np.cos(0.3), 0],
                    [0, 0, 0, 1],
                    ])
# Translation
assert np.allclose(params2affine([11, 12, 13, 0, 0, 0, 1, 1, 1]),
                   [[1, 0, 0, 11],
                    [0, 1, 0, 12],
                    [0, 0, 1, 13],
                    [0, 0, 0, 1]
                    ])
