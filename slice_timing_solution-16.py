#- Make acquisition_order vector, length 30, with values:
#- 0, 15, 1, 16 ... 14, 29
acquisition_order = np.zeros(30)
acquisition_index = 0
for i in range(0, 30, 2):
    acquisition_order[i] = acquisition_index
    acquisition_index += 1
for i in range(1, 30, 2):
    acquisition_order[i] = acquisition_index
    acquisition_index += 1
acquisition_order
# array([  0.,  15.,   1.,  16.,   2.,  17.,   3.,  18.,   4.,  19.,   5.,
# 20.,   6.,  21.,   7.,  22.,   8.,  23.,   9.,  24.,  10.,  25.,
# 11.,  26.,  12.,  27.,  13.,  28.,  14.,  29.])
