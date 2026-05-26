# A. Square
# https://codeforces.com/problemset/problem/1921/A
# rating: 800

t = int(input())

for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())

    print((max(x1, x2, x3, x4) - min(x1, x2, x3, x4)) ** 2)