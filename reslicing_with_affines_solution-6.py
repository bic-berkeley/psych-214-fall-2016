#- Load structural data, plot example slice
structural_data = structural_img.get_data()
plt.imshow(structural_data[:, :, 127])
# <...>
