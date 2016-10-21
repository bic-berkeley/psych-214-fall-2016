#- Compile the design matrix
#- First column is convolved regressor
#- Second column all ones
#- Hint: investigate "aspect" keyword to ``plt.imshow`` for a nice
#- looking image.
design = np.ones((len(convolved), 2))
design[:, 0] = convolved
plt.imshow(design, aspect=0.1)
# <...>
