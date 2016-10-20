n_trs = img.shape[-1]
data = img.get_data()
std_devs = []
for vol_no in range(n_trs):
    vol = data[..., vol_no]
    std_devs.append(np.std(vol))
# ...
plt.plot(std_devs)
# [...]
