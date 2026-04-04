# A. Equal Subsequences
# https://codeforces.com/problemset/problem/2118/A
# rating: 800

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if n == k:
        print("1" * k)
        continue

    if k == 0:
        print("0" * n)
        continue

    print("1" + "0" * (n- k - 1) + "1" * (k - 1) + "0")