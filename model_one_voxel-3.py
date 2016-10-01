convolved = np.loadtxt('ds114_sub009_t2r1_conv.txt')
# Knock off first 4 elements to match data
convolved = convolved[4:]
plt.plot(convolved)
# [...]
