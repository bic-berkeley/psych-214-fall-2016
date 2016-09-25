times = np.arange(0, 60, 0.5)  # samples every 0.5 seconds
neural_vector = np.zeros(times.shape)
neural_vector[10] = 1  # At 5 seconds
neural_vector[20] = 1  # At 10 seconds
plt.plot(times, neural_vector)
