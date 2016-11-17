# Show resampled data
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(resampled_mean_again[:, :, 150])
# <...>
axes[1].imshow(structural_data[:, :, 150])
# <...>
