import math

limit = 10001

temp = [0] * limit
temp[0] = 1
for i in range(2, int(math.sqrt(limit)) + 1):
    for j in range(2, 1 + (limit // i)):
        temp[(i * j) - 1] = 1
primes = [i + 1 for i, x in enumerate(temp) if x == 0]
primeset = set(primes)
