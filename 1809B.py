# B. Points on Plane
# https://codeforces.com/problemset/problem/1809/B
# rating: 1000

import math

t = int(input())

for _ in range(t):
    n = int(input())

    root = math.isqrt(n)

    if root * root == n:
        print(root - 1)
    else:
        print(root)