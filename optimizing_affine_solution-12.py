#- Plot slice from resampled subject data next to slice
#- from template data
fig, axes = plt.subplots(1, 2, figsize=(10, 15))
axes[0].imshow(subject_resampled[:, :, 42])
# <...>
axes[1].imshow(template_data[:, :, 42])
# <...>
