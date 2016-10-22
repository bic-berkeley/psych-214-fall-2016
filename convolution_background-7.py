TR = 2.5
tr_times = np.arange(0, 30, TR)
hrf_at_trs = hrf(tr_times)
len(hrf_at_trs)
# 12
plt.plot(tr_times, hrf_at_trs)
# [...]
plt.xlabel('time')
# <...>
plt.ylabel('HRF sampled every 2.5 seconds')
# <...>
