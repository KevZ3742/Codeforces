# A. Max and Mod
# https://codeforces.com/problemset/problem/2084/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2 == 0:
        print(-1)
    else:
        print(n, *range(1, n))