# A. Collecting Coins
# https://codeforces.com/problemset/problem/1294/A
# rating: 800

t = int(input())

for _ in range(t):
    a, b, c, n = map(int, input().split())

    equalizer = max(a, b, c)
    toSubtract = 3 * equalizer - (a + b + c)

    n -= toSubtract

    if n >= 0 and n % 3 == 0:
        print("YES")
    else:
        print("NO")