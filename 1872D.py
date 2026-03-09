# D. Plus Minus Permutation
# https://codeforces.com/problemset/problem/1872/D
# rating: 1200

import math

t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())

    common = n // math.lcm(x, y)
    lCount = n // x - common
    rCount = n // y - common

    left = ((n - lCount + 1) + n) * lCount // 2
    right = (1 + rCount) * rCount // 2

    print(left - right)
    