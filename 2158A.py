# A. Suspension
# https://codeforces.com/problemset/problem/2158/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    y, r = map(int, input().split())

    toPrint = r
    toPrint += min(y // 2, n - r)

    print(toPrint)