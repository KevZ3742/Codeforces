# B. Grid Reconstruction
# https://codeforces.com/problemset/problem/1816/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())

    evens = [*range(1, n + 1)]
    odds = [*range(n + 1, 2 * n + 1)]
    odds = [odds[-1]] + odds[:-1]

    evens[::2], odds[::2] = odds[::2], evens[::2]

    print(*evens)
    print(*odds)