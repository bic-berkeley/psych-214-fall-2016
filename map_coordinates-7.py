# Get the I, J, K coordinates implied by the structural data array
# shape
I, J, K = structural_data.shape
i_vals, j_vals, k_vals = np.meshgrid(range(I), range(J), range(K),
                                     indexing='ij')
in_vox_coords = np.array([i_vals, j_vals, k_vals])
in_vox_coords.shape
# (3, 256, 156, 256)
