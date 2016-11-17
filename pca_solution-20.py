#- Plot the signal in the first row against the signal in the second
#- Plot line corresponding to a scaled version of the first principal component
#- (Scaling may need to be negative)
plt.plot(X[0], X[1], '+')
# [...]
scaled_u = U[0, :] * -4000
plt.plot([0, scaled_u[0]], [0, scaled_u[1]], 'r')
# [...]
scaled_u[0]
# 3157.9395737...
