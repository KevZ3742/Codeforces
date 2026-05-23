# A. Magical Sticks
# https://codeforces.com/problemset/problem/1371/A
# rating: 800

import math

t = int(input())

for _ in range(t):
    n = int(input())

    print(math.ceil(n / 2))