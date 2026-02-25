# C. Test Generator
# https://codeforces.com/contest/2203/problem/C
# rating: ?

t = int(input())

for _ in range(t):
    s, m = map(int, input().split())

    a = m & -m

    if s % a != 0:
        print(-1)
    else:
        print((s + m - 1) // m)