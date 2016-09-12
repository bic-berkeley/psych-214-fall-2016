#- Here you might try plt.hist or something else to find a threshold
data_1d = data.ravel()
plt.hist(data_1d, bins=100)
# (...)
