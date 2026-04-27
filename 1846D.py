# D. Rudolph and Christmas Tree
# https://codeforces.com/problemset/problem/1846/D
# rating: 1200

t = int(input())

for _ in range(t):
    n, d, h = map(int, input().split())
    y = list(map(int, input().split()))
    
    toAdd = d * h / 2
    toPrint = toAdd
    prev = y[0]
    for i in range(1, n):
        toPrint += toAdd
        if y[i] - prev < h:
            b = (d * (prev + h - y[i])) / h
            toPrint -= (prev + h - y[i]) * b / 2

        prev = y[i]

    print(toPrint)