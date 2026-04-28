# D. Turtle Tenacity: Continual Mods
# https://codeforces.com/problemset/problem/1933/D
# rating: 1200

import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    gcd = math.gcd(*a)

    if a.count(gcd) >= 2:
        print("NO")
    else:
        print("YES")