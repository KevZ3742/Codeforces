# B. T-primes
# https://codeforces.com/problemset/problem/230/B
# rating: 1300

import math

n = int(input())
x = list(map(int, input().split()))

cap = 10 ** 6
primes = []
isPrime = [True] * (cap + 1)
for p in range(2, int(cap ** .5) + 1):
    if isPrime[p]:
        primes.append(p)
    
        for i in range(p * p, cap + 1, p):
            isPrime[i] = False

for num in x:
    if num == 1:
        print("NO")
        continue

    root = math.isqrt(num)

    if root * root == num and isPrime[root]:
        print("YES")
    else:
        print("NO")