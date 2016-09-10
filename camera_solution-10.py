#- Extra points - a good image of the man's pocket.
clipped_array = np.clip(pixel_array, 0, 0.1)
plt.imshow(clipped_array.T, cmap='gray')
# <...>
