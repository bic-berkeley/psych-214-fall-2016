last_but_1 = 0
fibonacci = 1
while fibonacci < 1000:
    last_but_2 = last_but_1
    last_but_1 = fibonacci
    fibonacci = last_but_2 + last_but_1
# ...
print("Largest Fibonacci < 1000 is", last_but_1)
# Largest Fibonacci < 1000 is 987
