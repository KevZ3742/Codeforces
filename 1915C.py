# C. Can I Square?
# https://codeforces.com/problemset/problem/1915/C
# rating: 800

import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    sqrt = math.isqrt(sum(a))

    if sum(a) == sqrt ** 2:
        print("YES")
    else:
        print("NO")