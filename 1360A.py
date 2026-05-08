# A. Minimal Square
# https://codeforces.com/problemset/problem/1360/A
# rating: 800


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print((min(max(2 * b,a ), max(2 * a,b))) ** 2)