# D. Remove Two Letters
# https://codeforces.com/problemset/problem/1800/D
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    overlap = 0
    for i in range(2, n):
        if s[i - 2] == s[i]:
            overlap += 1

    print(n - 1 - overlap)