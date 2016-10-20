#- Plot your function against the mt_hrf_estimates data to test
plt.plot(mt_hrf_times, mt_hrf(mt_hrf_times), label='mt_hrf')
# [...]
plt.plot(mt_hrf_times, mt_hrf_estimates, label='mt_hrf_estimates')
# [...]
plt.legend()
# <...>
