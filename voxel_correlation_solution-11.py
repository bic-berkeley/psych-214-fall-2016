# Loop over all voxel indices on the first, then second, then third dimension
# Extract the voxel time courses at each voxel coordinate in the image
# Get the correlation between the voxel time course and neural prediction
# Fill in the value in the correlations array
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        for k in range(data.shape[2]):
            vox_values = data[i, j, k]
            correlations[i, j, k] = np.corrcoef(time_course, vox_values)[1, 0]

# /Users/mb312/Library/Python/2.7/lib/python/site-packages/numpy/lib/function_base.py:1957: RuntimeWarning: invalid value encountered in true_divide
# return c / sqrt(multiply.outer(d, d))
