#- Read the stimulus data file and return a predicted neural time
#- course.
#- Plot the predicted neural time course.
neural_prediction = events2neural('ds114_sub009_t2r1_cond.txt', tr, data.shape[-1])
plt.plot(neural_prediction)
# [...]
plt.ylim(0, 1.2)
# (0, 1.2)
