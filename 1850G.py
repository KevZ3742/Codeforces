# G. The Morning Star
# https://codeforces.com/problemset/problem/1850/G
# rating: 1500

t = int(input())

for _ in range(t):
    n = int(input())

    cardinals = {}
    toPrint = 0

    for i in range(n):
        x, y = map(int, input().split())

        for i, j in enumerate((x, y, x+y, x-y)):
            cardinals[(i, j)] = cardinals.get((i, j), 0) + 1
    
    for v in cardinals.values():
        toPrint += v * (v - 1)

    print(toPrint)