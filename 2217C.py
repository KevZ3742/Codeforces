# C. Grid Covering
# https://codeforces.com/problemset/problem/2217/C
# rating: 1300

from math import gcd

t = int(input())

for _ in range(t):
    n, m, a, b = map(int, input().split())

    if gcd(n, a) == 1 and gcd(m, b) == 1 and gcd(n, m) <= 2:
        print("YES")
    else:
        print("NO")