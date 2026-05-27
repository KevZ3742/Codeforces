# A. Favorite Sequence
# https://codeforces.com/problemset/problem/1462/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    l = 0
    r = n - 1
    toPrint = []

    while l < r:
        toPrint.append(str(b[l]))
        toPrint.append(str(b[r]))
        l += 1
        r -= 1

    if l == r:
        toPrint.append(str(b[l]))

    print(" ".join(toPrint))