# A. Two Elevators
# https://codeforces.com/problemset/problem/1729/A
# rating: 800

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    first = abs(a - 1)
    second = abs(b - c) + abs(c - 1)

    if first < second:
        print(1)
    elif second < first:
        print(2)
    else:
        print(3)