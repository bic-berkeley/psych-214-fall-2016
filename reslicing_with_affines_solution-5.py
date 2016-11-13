#- Load BOLD image data.  Drop first volume.  Make mean volume
#- Plot an example slice from the mean volume
bold_data = bold_img.get_data()
mean_vol = bold_data[..., 1:].mean(axis=-1)
plt.imshow(mean_vol[:, :, 14])
# <...>
