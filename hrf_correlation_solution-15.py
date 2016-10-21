#- Sample HRF at given times
#- Plot HRF samples against times
hrf_signal = mt_hrf(hrf_times)
plt.plot(hrf_times, hrf_signal)
# [...]
