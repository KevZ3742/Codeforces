# C. Contrast Value
# https://codeforces.com/problemset/problem/1832/C
# rating: 1200

from itertools import groupby

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = []
    for key, group in groupby(a):
        b.append(key)

    if len(b) == 1:
        print(1)
        continue

    toPrint = 2
    for i in range(1, len(b) - 1):
        if b[i - 1] < b[i] > b[i + 1] or b[i - 1] > b[i] < b[i + 1]:
            toPrint += 1

    print(toPrint)