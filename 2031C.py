# C. Penchick and BBQ Buns
# https://codeforces.com/problemset/problem/2031/C
# rating: 1300

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = []

    if n % 2:
        if n <= 25:
            print(-1)
            continue

        pattern = [1, 3, 3, 4, 4, 5, 5, 6, 6, 1, 2, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 1, 2]

        for i in range(14, n // 2 + 1):
            pattern.append(i)
            pattern.append(i)

        print(*pattern)
    else:
        for i in range(1, n // 2 + 1):
            toPrint.append(i)
            toPrint.append(i)

        print(*toPrint)