output_shape = (5, 6, 7)
I, J, K = output_shape
i_coords, j_coords, k_coords = np.meshgrid(range(I),
                                           range(J),
                                           range(K),
                                           indexing='ij')
coordinate_grid = np.array([i_coords, j_coords, k_coords])
coordinate_grid.shape
# (3, 5, 6, 7)
