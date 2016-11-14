#- show example slice from template and normalized image
fig, axes = plt.subplots(1, 2, figsize=(10, 15))
axes[0].imshow(best_subject_data[:, :, 42])
# <...>
axes[1].imshow(template_data[:, :, 42])
# <...>
