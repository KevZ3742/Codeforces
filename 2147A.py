# A. Shortest Increasing Path
# https://codeforces.com/problemset/problem/2147/A
# rating: 800

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if x == y or x == y + 1 or y == 1:
        print(-1)
        continue

    if x < y:
        print(2)
    else:
        print(3)