# C. Palindromic Subsequences
# https://codeforces.com/problemset/problem/2056/C
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = [1]
    marker = n // 2
    marker2 = n - marker - 1

    for i in range(1, marker + 1):
        toPrint.append(i)

    for i in range(1, marker2 + 1):
        toPrint.append(i)

    print(*toPrint)