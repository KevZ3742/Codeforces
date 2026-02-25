# A. Towers of Boxes
# https://codeforces.com/contest/2203/problem/A
# rating: ?

import math

t = int(input())

for _ in range(t):
    n, m, d = map(int, input().split())

    h = d // m + 1
    toPrint = math.ceil(n / h)

    print(toPrint)