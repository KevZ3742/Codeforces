# B. The 67th 6-7 Integer Problem
# https://codeforces.com/contest/2218/problem/B
# rating: ?

t = int(input())

for _ in range(t):
    a = sorted(map(int, input().split()))

    print(-sum(a[:-1]) + a[-1])
