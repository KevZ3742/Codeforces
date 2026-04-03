# B. Alternating Series
# https://codeforces.com/problemset/problem/2131/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = []
    for i in range(n):
        if i % 2 == 0:
            toPrint.append(-1)
        else:
            toPrint.append(3)

    if toPrint[-1] == 3:
        toPrint[-1] = 2

    print(*toPrint)