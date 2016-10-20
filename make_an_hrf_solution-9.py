#- Evidence that your function is better than mine?
np.corrcoef(mt_hrf_times, not_great_hrf(mt_hrf_times))
# array([[ 1.    , -0.4985],
# [-0.4985,  1.    ]])
np.corrcoef(mt_hrf_times, mt_hrf(mt_hrf_times))
# array([[ 1.    , -0.6344],
# [-0.6344,  1.    ]])
