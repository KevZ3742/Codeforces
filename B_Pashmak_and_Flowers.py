# https://codeforces.com/problemset/problem/459/B
# rating: 1300

import math

n = int(input())
b = list(map(int, input().split()))

b.sort()

maxCount = 0
minCount = 0

i = 0
while b[i] == b[0]:
    minCount += 1
    i += 1

    if i == n:
        break

j = n - 1
while b[j] == b[-1]:
    maxCount += 1
    j -= 1

    if j == -1:
        break

if b[0] == b[-1]:
    print(b[-1] - b [0], math.comb(n, 2))
else:
    print(b[-1] - b [0], minCount * maxCount)