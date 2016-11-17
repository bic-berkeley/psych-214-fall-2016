# Optimization above varies slightly across platforms; test here.
np.allclose(best_params,
            [ -2.0349, 38.6679, -18.986 , 0.0287, -0.0075, 0.028,
               0.9215, 0.9484, 0.8877], atol=0.005)
# True
