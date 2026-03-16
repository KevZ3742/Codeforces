# C. Superultra's Favorite Permutation
# https://codeforces.com/problemset/problem/2037/C
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())

    if n < 5:
        print(-1)
        continue

    toPrint = []
    for i in range(2, n + 1, 2):
        if i != 4:
            toPrint.append(i)

    toPrint.append(4)
    toPrint.append(5)

    for i in range(1, n + 1, 2):
        if i != 5:
            toPrint.append(i)

    print(*toPrint)