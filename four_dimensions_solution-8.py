#- Read global signal values calculated by SPM, and plot
global_signals = np.loadtxt('global_signals.txt')
plt.plot(global_signals)
# [...]
