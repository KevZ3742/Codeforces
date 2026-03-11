# B. Make It Permutation
# https://codeforces.com/problemset/problem/2118/B
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())

    print(2 * n - 1)

    for i in range(1, n):
        print(i, 1, i)
        print(i, i + 1, n)

    print(n, 1, n)