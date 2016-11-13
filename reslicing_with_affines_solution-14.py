#- Display example slices for resliced mean and structural
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(mean_in_struct_space[:, :, 127])
# <...>
axes[1].imshow(structural_data[:, :, 127])
# <...>
