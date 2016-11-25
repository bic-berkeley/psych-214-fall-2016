#- Subtract two versions of the smoothed slice, show
diff_slice = smoothed_slice - scipy_slice
plt.imshow(diff_slice)
# <...>
