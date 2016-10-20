from stimuli import events2neural
n_vols = 173
neural_prediction = events2neural('ds114_sub009_t2r1_cond.txt',
                                  TR, n_vols)
all_tr_times = np.arange(173) * TR
plt.plot(all_tr_times, neural_prediction)
# [...]
