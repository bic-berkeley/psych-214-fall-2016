import scipy.stats as sst
tdistrib = sst.t(df_error)
# 1 - cumulative density function (P(x <= t)
1. - tdistrib.cdf(tstat)
# is the same as the "survival function"
tdistrib.sf(tstat)
