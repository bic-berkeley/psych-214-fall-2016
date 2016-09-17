#- Get standard deviation for each volume; then plot the values
stds = []
for i in range(data.shape[-1]):
    vol = data[..., i]
    stds.append(np.std(vol))
plt.plot(stds)
# [...]
