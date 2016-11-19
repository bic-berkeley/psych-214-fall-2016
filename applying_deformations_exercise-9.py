#: to mat and vec
mat, vec = nib.affines.to_matvec(vox2vox)
mat
# array([[-1.5,  0. ,  0. ],
# [ 0. ,  1.5,  0. ],
# [ 0. ,  0. ,  1.5]])
vec
# array([ 188.,    8.,    0.])
