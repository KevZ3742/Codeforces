# A. Cards for Friends
# https://codeforces.com/problemset/problem/1472/A
# rating: 800

t = int(input())

for _ in range(t):
    w, h, n = map(int, input().split())

    pieces = 1

    while w % 2 == 0:
        pieces *= 2
        w //= 2

    while h % 2 == 0:
        pieces *= 2
        h //= 2

    print("YES" if pieces >= n else "NO")