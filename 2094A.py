# A. Trippi Troppi
# https://codeforces.com/problemset/problem/2094/A
# rating: 800

t = int(input())

for _ in range(t):
    arr = list(input().split())

    toPrint = []
    for a in arr:
        toPrint.append(a[0])

    print("".join(toPrint))