#- Make a new array `smoothed_slice` for smoothed output
#- Loop over first dimension applying kernel as above
#- Loop over second dimension of smoothed image, applying kernel
#- Show with `imshow`
smoothed_slice = np.zeros(mid_slice.shape)
n_x, n_y = mid_slice.shape
for x in range(n_x):
    line = mid_slice[x, :]
    smoothed = np.convolve(line, kernel)
    smoothed_slice[x, :] = smoothed[kernel_offset:n_y+kernel_offset]
for y in range(n_y):
    line = smoothed_slice[:, y]
    smoothed = np.convolve(line, kernel)
    smoothed_slice[:, y] = smoothed[kernel_offset:n_x+kernel_offset]
plt.imshow(smoothed_slice)
# <...>
