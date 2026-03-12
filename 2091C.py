# C. Combination Lock
# https://codeforces.com/problemset/problem/2091/C
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2:
        print(*list(range(1, n + 1, 2)) + list(range(2, n, 2)))
    else:
        print(-1)