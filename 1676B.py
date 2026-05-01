# B. Equal Candies
# https://codeforces.com/problemset/problem/1676/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    toPrint = 0
    for candles in a:
        toPrint += candles - a[0]

    print(toPrint)