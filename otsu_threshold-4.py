total_ssds = []
for bin_no in range(1, n_bins):
    left_ssd = ssd(counts[:bin_no], bin_centers[:bin_no])
    right_ssd = ssd(counts[bin_no:], bin_centers[bin_no:])
    total_ssds.append(left_ssd + right_ssd)
z = np.argmin(total_ssds)
t = bin_centers[z]
print('Otsu bin (z):', z)
# Otsu bin (z): 43
print('Otsu threshold (c[z]):', bin_centers[z])
# Otsu threshold (c[z]): 0.33984375
