#- Apply threshold to make new binary image, and show binary image
binary_array = pixel_array > 0.1
plt.imshow(binary_array.T, cmap='gray')
# <...>
