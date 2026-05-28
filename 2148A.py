# A. Sublime Sequence
# https://codeforces.com/problemset/problem/2148/A
# rating: 800

t = int(input())

for _ in range(t):
    x, n = map(int, input().split())

    if n % 2:
        print(x)
    else:
        print(0)