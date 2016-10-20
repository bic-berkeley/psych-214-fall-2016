#- Convolve predicted neural time course with HRF samples
hemodynamic_prediction = np.convolve(neural_prediction_no_0, hrf_signal)
