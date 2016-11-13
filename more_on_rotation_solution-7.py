#: slices on z, y, and x axis for original and rotated images
fig, axes = plt.subplots(3, 2, figsize=(10, 15))
axes[0, 0].imshow(vol0[:, :, 17])
# <...>
axes[0, 1].imshow(rotated_vol0[:, :, 17])
# <...>
axes[1, 0].imshow(vol0[:, 31, :])
# <...>
axes[1, 1].imshow(rotated_vol0[:, 31, :])
# <...>
axes[2, 0].imshow(vol0[31, :, :])
# <...>
axes[2, 1].imshow(rotated_vol0[31, :, :])
# <...>
