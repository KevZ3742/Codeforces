# A. Desorting
# https://codeforces.com/problemset/problem/1853/A
# rating: 800

import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    flag = False
    prefixDiff = []
    for i in range(1, n):
        toAppend = a[i] - a[i - 1]

        if toAppend < 0:
            flag = True
            break

        prefixDiff.append(toAppend)

    if flag:
        print(0)
        continue

    print(min(prefixDiff) // 2 + 1)