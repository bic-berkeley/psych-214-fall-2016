# Load the neural time course using pre-packaged function
from stimuli import events2neural
TR = 2.5  # time between volumes
n_trs = img.shape[-1]  # The original number of TRs
neural = events2neural('ds114_sub009_t2r1_cond.txt', TR, n_trs)
plt.plot(neural)
# [...]
