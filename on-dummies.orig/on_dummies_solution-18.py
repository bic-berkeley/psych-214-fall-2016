def two_group_ct_ixtx_c(b, n):
   return 1. / b + 1. / (n - b)
# ...
two_group_ct_ixtx_c(np.arange(1, 10), 10)
# array([ 1.1111,  0.625 ,  0.4762,  0.4167,  0.4   ,  0.4167,  0.4762,
# 0.625 ,  1.1111])
