# A. Yet Another Two Integers Problem
# https://codeforces.com/problemset/problem/1409/A
# rating: 800

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    target = abs(a - b)
    toPrint = target // 10

    if toPrint * 10 == target:
        print(toPrint)
    else:
        print(toPrint + 1)