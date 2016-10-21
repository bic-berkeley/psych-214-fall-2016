#- Plot convolved neural prediction and unconvolved neural prediction
plt.plot(neural_prediction, label='unconvolved')
# [...]
plt.plot(hemodynamic_prediction, label='convolved')
# [...]
plt.legend()
# <...>
