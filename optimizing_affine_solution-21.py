#- Call optimizing function and collect best estimates for rotations
#- Collect best estimates in `best_params` variable
best_params = fmin_powell(cost_function, [0, 0, 0, 0, 0, 0, 1, 1, 1],
                          callback=my_callback)
# Trying parameters [ ... ]
# Optimization terminated successfully.
# Current function value: -0.9...
# Iterations: 4
# Function evaluations: ...
best_params  # doctest: +SKIP
# array([ -2.0349,  38.6679, -18.986 ,   0.0287,  -0.0075,   0.028 ,
# 0.9215,   0.9484,   0.8877])
