#- Maybe display some slices from the data binarized with a threshold
threshold = 300
binarized_data = data > threshold
plt.imshow(binarized_data[:, :, 30], cmap='gray')
# <...>
