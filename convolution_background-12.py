# Save the convolved time course to 6 decimal point precision
np.savetxt('ds114_sub009_t2r1_conv.txt', convolved, fmt='%2.6f')
back = np.loadtxt('ds114_sub009_t2r1_conv.txt')
np.allclose(convolved, back)
# True
