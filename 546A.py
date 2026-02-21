# A. Soldier and Bananas
# https://codeforces.com/contest/546/problem/A
# rating: 800

k, n, w = map(int, input().split())

n -= k * w * (w + 1) // 2

if n < 0:
    print(abs(n))
else:
    print(0)