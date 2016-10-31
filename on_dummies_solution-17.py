#- Use scipy.stats to test if your t-test value is significant.
import scipy.stats as sst
tdistrib = sst.t(df_error)
# 1 - cumulative density function (P(x <= t)
1. - tdistrib.cdf(tstat)
# 0.08635...
# This is the same as the "survival function"
tdistrib.sf(tstat)
# 0.08635...
