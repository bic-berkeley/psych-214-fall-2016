#- Reshape first dimension of whole image data array to N, and take
#- transpose
arr = data.reshape(N, n_vols).T
arr.shape
# (173, 122880)
