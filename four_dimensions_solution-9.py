#- Apply algorithm for SPM global calculation to first volume
vol = data[..., 0]
T = np.mean(vol)/ 8
msk = vol > T
W = vol[msk]
np.mean(W)
# 376.53382753...
