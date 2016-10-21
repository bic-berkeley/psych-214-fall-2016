#- Load the pre-written convolved time course
#- Knock off the first four elements
convolved = np.loadtxt('ds114_sub009_t2r1_conv.txt')[4:]
plt.plot(convolved)
# [...]
