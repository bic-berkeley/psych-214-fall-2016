# The mismatch metric
metric = CCMetric(3)
# The optimization strategy:
level_iters = [10, 10, 5]
# Registration object
sdr = SymmetricDiffeomorphicRegistration(metric, level_iters)
