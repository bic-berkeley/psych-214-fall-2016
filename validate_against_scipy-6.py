res = scipy.stats.linregress(x, y)
res.slope
# 0.07227...
res.intercept
# 19.35665...
# This is the same as the manual GLM fit
np.allclose(B, [res.intercept, res.slope])
# True
# p value is always two-tailed
res.pvalue
# 0.42171...
np.allclose(p_value * 2, res.pvalue)
# True
