cond_data = np.loadtxt('new_cond.txt')
cond_data
# array([[   3.35,    3.  ,    2.  ],
# [  12.76,    3.  ,    2.  ],
# [  43.27,    3.  ,    2.  ],
# [  75.25,    3.  ,    1.  ],
# [  95.48,    3.  ,    2.  ],
# [ 167.84,    3.  ,    2.  ],
# [ 282.36,    3.  ,    2.  ],
# [ 304.76,    3.  ,    2.  ],
# [ 356.32,    3.  ,    2.  ],
# [ 372.22,    3.  ,    3.  ]])
onsets_seconds = cond_data[:, 0]
durations_seconds = cond_data[:, 1]
amplitudes = cond_data[:, 2]
