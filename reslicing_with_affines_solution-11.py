#- Display example slice from mean vol and resliced structural side by
#- side.
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(struct_in_mean_space[:, :, 14])
# <...>
axes[1].imshow(mean_vol[:, :, 14])
# <...>
