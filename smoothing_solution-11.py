#- Work out the +/- limit for the kernel x values;
#- Make a vector `x` to sample the PDF;
#- Get `kernel` vector by sampling the PDF at these x values (mu=0);
#- Work out `kernel_offset`.
# >>>
limit = round(sigma * 4)
# Make an x range between -sigma * 3 and +sigma * 3
x_for_kernel = np.arange(-limit, limit+1)
# Calculate kernel
kernel = norm_pdf(x_for_kernel, 0, sigma)
# Plot kernel
plt.plot(x_for_kernel, kernel)
# [...]
# Calculate `kernel_offset`
kernel_offset = int(limit)
kernel_offset
# 14
