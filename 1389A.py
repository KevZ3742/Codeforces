# A. LCM Problem
# https://codeforces.com/problemset/problem/1389/A
# rating: 800

t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    if 2 * l <= r:
        print(l, 2 * l)
    else:
        print(-1, -1)