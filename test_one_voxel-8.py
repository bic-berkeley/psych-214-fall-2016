from scipy.stats import t as t_dist
# Get p value for t value using cumulative density dunction
# (CDF) of t distribution
ltp = t_dist.cdf(t_stat, df) # lower tail p
p = 1 - ltp # upper tail p
p
# 0.0
