import sympy
n, b = sympy.symbols('n, b')
# construct the equation in terms of n and b
eqn = 1 / b + 1 / (n - b)
# differentiate with respect to b
d_db = sympy.diff(eqn, b)
d_db
# (-b + n)**(-2) - 1/b**2
# find values of b at which differential is 0.
sympy.solve(d_db, b)
# [n/2]
