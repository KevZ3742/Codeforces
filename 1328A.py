# A. Divisibility Problem
# https://codeforces.com/contest/1328/problem/A
# rating: 800

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a % b == 0:
        print(0)
    else:
        print(b - a % b)