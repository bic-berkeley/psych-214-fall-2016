# Save the convolved time course to 6 decimal point precision
np.savetxt('ds114_sub009_t2r1_conv.txt', convolved, fmt='%2.6f')
back = np.loadtxt('ds114_sub009_t2r1_conv.txt')
# Check written data is within 0.000001 of original
np.allclose(convolved, back, atol=1e-6)
# True
