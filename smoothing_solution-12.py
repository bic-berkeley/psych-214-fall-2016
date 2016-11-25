#- Convolve image line with kernel
#- Slice out the result we want using kernel_offset
#- Plot smoothed with unsmoothed line
smoothed = np.convolve(mid_line, kernel)
smoothed = smoothed[kernel_offset:len(mid_line)+kernel_offset]
plt.plot(mid_line)
# [...]
plt.plot(smoothed)
# [...]
