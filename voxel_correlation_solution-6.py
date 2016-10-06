#- Call the events2neural function to generate the on-off values for
#- each volume.  Plot these values.
time_course = events2neural('ds114_sub009_t2r1_cond.txt', 2.5, n_trs)
plt.plot(time_course)
# [...]
