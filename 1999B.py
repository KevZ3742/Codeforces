# B. Card Game
# https://codeforces.com/problemset/problem/1999/B
# rating: 1000

t = int(input())

for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())

    toPrint = 0
    if (a1 > b1) - (a1 < b1) + (a2 > b2) - (a2 < b2) > 0:
        toPrint += 1
    if (a1 > b2) - (a1 < b2) + (a2 > b1) - (a2 < b1) > 0:
        toPrint += 1
    if (a2 > b1) - (a2 < b1) + (a1 > b2) - (a1 < b2) > 0:
        toPrint += 1
    if (a2 > b2) - (a2 < b2) + (a1 > b1) - (a1 < b1) > 0:
        toPrint += 1

    print(toPrint)