# B. Good Kid
# https://codeforces.com/problemset/problem/1873/B
# rating: 800

import math

t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    minIndex = a.index(min(a))
    a[minIndex] += 1

    print(math.prod(a))