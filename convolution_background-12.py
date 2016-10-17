np.savetxt('ds114_sub009_t2r1_conv.txt', convolved)
back = np.loadtxt('ds114_sub009_t2r1_conv.txt')
np.allclose(convolved, back)
# True
