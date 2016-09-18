#- Make an `spm_global` function that accepts a 3D array as input,
#- and returns the global mean for the volume according to the SPM
#- algorithm
def spm_global(vol):
    T = np.mean(vol) / 8
    return np.mean(vol[vol > T])
# ...
print(spm_global(data[:, :, :, 0]))
# 376.533827532
