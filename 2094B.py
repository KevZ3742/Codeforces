# B. Bobritto Bandito
# https://codeforces.com/problemset/problem/2094/B
# rating: 800

t = int(input())

for _ in range(t):
    n, m, l, r  = map(int, input().split())

    r = min(m, r)
    rest = m - r
    l = 0 - rest

    print(l, r)