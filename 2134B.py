# B. Add 0 or K
# https://codeforces.com/problemset/problem/2134/B
# rating: 1200

import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    x = 2
    while math.gcd(k, x) != 1:
        x += 1

    toPrint = []
    for num in a:
        counter = 0
        while (k * counter + num) % x != 0:
            counter += 1

        toPrint.append(k * counter + num)

    print(*toPrint)