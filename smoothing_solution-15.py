#- Use gaussian filter to smooth `mid_slice`
scipy_slice = gaussian_filter(mid_slice, sigma)
plt.imshow(scipy_slice)
# <...>
