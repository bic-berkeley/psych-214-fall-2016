# Fill in values of 1 for positions of on blocks in time course
for onset, duration in ons_durs:
    time_course[onset:onset + duration] = 1
