n = 10
y = sample
y_bar = y.mean()
unbiased_var_estimate = 1. / (n - 1) * np.sum((y - y_bar) ** 2)
unbiased_sd_est = np.sqrt(unbiased_var_estimate)
