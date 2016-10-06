#- Use subplots to make axes to plot first 10 principal component
#- vectors
#- Plot one component vector per sub-plot.
fig, axes = plt.subplots(10, 1)
for i, ax in enumerate(axes):
    ax.plot(U[:, i])
# [...]
