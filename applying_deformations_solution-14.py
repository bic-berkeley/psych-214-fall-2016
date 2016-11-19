#- show an example slice from the resampled template and resampled
#- subject
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(template_into_tpm[:, :, 60])
# <...>
axes[1].imshow(subject_into_tpm[:, :, 60])
# <...>
