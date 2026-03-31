# B. Permutation Printing
# https://codeforces.com/problemset/problem/1930/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = []
    for i in range(1, (n // 2) + 1):
        toPrint.append(i)
        toPrint.append(i + (n + 1) // 2)

    if n % 2:
        toPrint.append((n + 1) // 2)

    print(*toPrint)