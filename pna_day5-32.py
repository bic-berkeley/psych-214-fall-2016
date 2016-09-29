def hrf(t):
    "A hemodynamic response function"
    values = t ** 8.6 * np.exp(-t / 0.547)
    # Scale max to 1
    return values / np.max(values)
# ...
hrf_times = np.arange(0, 20, 0.5)
hrf_samples = hrf(hrf_times)
plt.plot(hrf_times, hrf_samples)
