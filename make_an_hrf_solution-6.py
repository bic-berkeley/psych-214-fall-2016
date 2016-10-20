#: plot the data against my estimate
plt.plot(mt_hrf_times, not_great_hrf(mt_hrf_times), label='not_great_hrf')
# [...]
plt.plot(mt_hrf_times, mt_hrf_estimates, label='mt_hrf_estimates')
# [...]
plt.legend()
# <...>
