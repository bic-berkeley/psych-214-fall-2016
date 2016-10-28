import scipy.stats
t_dist = scipy.stats.t(df=df)
p_value = 1 - t_dist.cdf(t)
# One-tailed t-test (t is positive)
p_value
# 0.21085...
# Two-tailed p value is just 2 * one tailed value, because
# distribution is symmetric
2 * p_value
# 0.42171...
