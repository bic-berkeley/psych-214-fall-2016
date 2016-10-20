#- Load the estimated values from the text file into an array
#- Make an array of corresponding times
#- Plot signal by time
mt_hrf_estimates = np.loadtxt('mt_hrf_estimates.txt')
mt_hrf_times = np.arange(0, 30, 2)
plt.plot(mt_hrf_times, mt_hrf_estimates)
# [...]
