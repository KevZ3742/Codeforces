# A. Yogurt Sale
# https://codeforces.com/problemset/problem/1955/A
# rating: 800

t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    if n == 1:
        print(a)
        continue

    if 2 * a < b:
        print(n * a)
    else:
        print(b * (n // 2) + a * (n % 2))