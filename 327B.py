# B. Hungry Sequence
# https://codeforces.com/contest/327/problem/B
# rating: 1200

import math

n = int(input())

if n == 1:
    print(2)
    exit()

upperBound = int(n * (math.log(n) + math.log(math.log(n)))) + 3

primes = []
isPrime = [True] * (upperBound + 1)

for p in range(2, upperBound + 1):
    if isPrime[p]:
        primes.append(p)

        if len(primes) == n:
            break

        for i in range(p * p, upperBound + 1, p):
            isPrime[i] = False

print(*primes)