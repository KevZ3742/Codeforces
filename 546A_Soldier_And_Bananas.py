# https://codeforces.com/problemset/problem/546/A
# rating: 800

k, n, w = map(int, input().split())

n -= k * w * (w + 1) // 2

if n < 0:
    print(abs(n))
else:
    print(0)