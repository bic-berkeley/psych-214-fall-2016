try3 = np.reshape(pixel_array, (170, 156, 32))
plt.imshow(try3[:, :, 15])
# <...>

# The last one looks good, so final shape is:
try3.shape
# (170, 156, 32)
