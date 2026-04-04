# A. Bestie
# https://codeforces.com/problemset/problem/1732/A
# rating: 1000

import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if math.gcd(*a) == 1:
        print(0)
        continue

    if n == 1:
        print(1)
        continue

    a1 = a.copy()
    a1[-1] = math.gcd(a[-1], n)

    if math.gcd(*a1) == 1:
        print(1)
        continue

    a2 = a.copy()
    a2[-2] = math.gcd(a[-2], n - 1)

    if math.gcd(*a2) == 1:
        print(2)
        continue

    print(3)

