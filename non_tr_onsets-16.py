tr_indices = np.arange(n_trs)
hr_tr_indices = np.round(tr_indices * tr_divs).astype(int)
tr_hemo = high_res_hemo[hr_tr_indices]
tr_times = tr_indices * TR  # times of TR onsets in seconds
plt.plot(tr_times, tr_hemo)
# [...]
plt.xlabel('Time (seconds)')
# <...>
plt.ylabel('Convolved values at TR onsets')
# <...>
