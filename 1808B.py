# B. Playing in a Casino
# https://codeforces.com/problemset/problem/1808/B
# rating: 1200

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    cards = []    
    for i in range(n):
        c = list(map(int, input().split()))

        cards.append(c)

    toPrint = 0
    for i in range(m):
        column = [row[i] for row in cards]
        column.sort()

        for j in range(n):
            toPrint += j * column[j] - (n - j - 1) * column[j]

    print(toPrint)