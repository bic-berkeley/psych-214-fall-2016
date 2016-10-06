#- Write a function `get_spm_globals` that returns the global values
#- for each volume
def get_spm_globals(fname):
    img = nib.load(fname)
    data = img.get_data()
    spm_vals = []
    for i in range(data.shape[-1]):
        vol = data[..., i]
        spm_vals.append(spm_global(vol))
    return spm_vals
# ...
all_globals = get_spm_globals('ds107_sub012_t1r2.nii')
plt.plot(all_globals)
# [...]
