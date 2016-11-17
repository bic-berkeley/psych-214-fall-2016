#- Call optimizing function and collect best estimates for rotations
#- Collect best estimates in `best_params` variable
best_params = fmin_powell(cost_function, [0, 0, 0, 0, 0, 0, 1, 1, 1],
                          callback=my_callback)
# Trying parameters [ -0.417   41.5029 -22.1551   0.0015  -0.0017   0.0033   0.8909   0.9572
# 0.9033]
# Trying parameters [ -1.7615  39.1924 -19.4564   0.0246  -0.0098   0.0222   0.9218   0.9484
# 0.8877]
# Trying parameters [ -2.035   38.6871 -18.9906   0.0287  -0.0075   0.028    0.9215   0.9484
# 0.8877]
# Trying parameters [ -2.0349  38.6679 -18.986    0.0287  -0.0075   0.028    0.9215   0.9484
# 0.8877]
# Optimization terminated successfully.
# Current function value: -0.925598
# Iterations: 4
# Function evaluations: 737
best_params
# array([ -2.0349,  38.6679, -18.986 ,   0.0287,  -0.0075,   0.028 ,
# 0.9215,   0.9484,   0.8877])
