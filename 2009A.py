# A. Minimize!
# https://codeforces.com/problemset/problem/2009/A
# rating: 800

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print(b - a)