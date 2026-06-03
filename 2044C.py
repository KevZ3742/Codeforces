# C. Hard Problem
# https://codeforces.com/problemset/problem/2044/C
# rating: 800

t = int(input())

for _ in range(t):
    m, a, b, c = map(int, input().split())

    fixed = min(a, m) + min(b, m)
    remaining = 2 * m - fixed

    print(fixed + min(c, remaining))