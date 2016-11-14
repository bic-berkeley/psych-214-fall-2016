x = differences
n = len(x)
x_bar = np.mean(x)
x_bar
# 0.70314...
unviased_var_x = 1. / (n - 1) * np.sum((x - x_bar) ** 2)
s_x = np.sqrt(unviased_var_x)
s_x
# 1.17718...
SEM = s_x / np.sqrt(n)
SEM
# 0.37225...
t = x_bar / SEM
t
# 1.88884...
