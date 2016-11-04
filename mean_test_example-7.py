n_samples = 100000
pop_mean = 5
pop_sd = 1.5
means_of_samples = np.zeros(n_samples)
for i in range(n_samples):
    sample = np.random.normal(pop_mean, pop_sd, size=n)
    means_of_samples[i] = sample.mean()
sq_deviations = (means_of_samples - pop_mean) ** 2
# With lots of samples, this value is close to the exact number
means_std_dev = np.sqrt(1. / n_samples * np.sum(sq_deviations))
means_std_dev
# 0.474735...
