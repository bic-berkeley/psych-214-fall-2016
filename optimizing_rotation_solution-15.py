#- Call optimizing function and collect best estimates for rotations
best_params = fmin_powell(cost_function, [0, 0, 0])
# Optimization terminated successfully.
# Current function value: -0.919532
# Iterations: 5
# Function evaluations: 318
best_params
# array([-0.01  , -0.1038,  0.1975])
