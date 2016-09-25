#- Subtract the means for each row, put the result into X
#- Show the means over the columns, after the subtraction
X = first_two - row_means
np.mean(X, axis=1)
# memmap([-0.,  0.])
