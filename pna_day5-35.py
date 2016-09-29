hemodynamic_for_60s = hemodynamic_prediction[:len(neural_vector)]
plt.plot(times, neural_vector, label='neural vector')
plt.plot(times, hemodynamic_for_60s, label='hemodynamic prediction')
plt.legend()
