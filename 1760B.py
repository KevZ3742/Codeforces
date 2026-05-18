# B. Atilla's Favorite Problem
# https://codeforces.com/problemset/problem/1760/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    maxChar = 97
    for c in s:
        maxChar = max(maxChar, ord(c))

    print(maxChar - 96)

    