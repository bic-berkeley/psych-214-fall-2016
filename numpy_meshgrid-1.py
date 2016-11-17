import numpy as np
i_coords, j_coords = np.meshgrid(range(5), range(4), indexing='ij')
i_coords
# array([[0, 0, 0, 0],
# [1, 1, 1, 1],
# [2, 2, 2, 2],
# [3, 3, 3, 3],
# [4, 4, 4, 4]])
j_coords
# array([[0, 1, 2, 3],
# [0, 1, 2, 3],
# [0, 1, 2, 3],
# [0, 1, 2, 3],
# [0, 1, 2, 3]])
