# E. Divisive Battle
# https://codeforces.com/contest/2200/problem/E
# rating: ?

import math

def primeFactorization(n):
    factors = set()

    while n % 2 == 0:
        factors.add(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i

    if n > 2:
        factors.add(n)

    if len(factors) > 1:
        return -1
    
    if len(factors) == 0:
        return 1
    
    return factors.pop()

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a == sorted(a):
        print("Bob")
        continue

    factors = []
    for element in a:
        factors.append(primeFactorization(element))

    if min(factors) == -1:
        print("Alice")
    elif factors == sorted(factors):
        print("Bob")
    else:
        print("Alice")