primes = []
for x in range(2, 30):
    for p in primes:
        # x exactly divisible by prime -> x not prime
        if (x % p) == 0:
            break
    else:
        # else: block executes if no 'break" in previous loop
        primes.append(x)
# ...
print("Primes in 2 through 30", primes)
# Primes in 2 through 30 [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
