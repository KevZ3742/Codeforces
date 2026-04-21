# C. Earning on Bets
# https://codeforces.com/problemset/problem/1979/C
# rating: 1200

from math import lcm

t = int(input())

for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))

    tot = lcm(*k)
    bets = [tot // i for i in k]

    if sum(bets) >= tot:
        print(-1)
    else:
        print(*bets)