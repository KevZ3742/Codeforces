# A. Legs
# https://codeforces.com/problemset/problem/1996/A
# rating: 800

import math

t = int(input())

for _ in range(t):
    n = int(input())

    print(math.ceil(n / 4))