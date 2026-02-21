# B. Present from Lena
# https://codeforces.com/contest/118/problem/B
# rating: 1000

n = int(input())

spaces = n * 2
for i in range(n + 1):
    toPrint = " " * spaces
    spaces -= 2

    for j in range(i + 1):
        toPrint += str(j) + " "

    for j in range(i - 1, -1, -1):
        toPrint += str(j) + " "

    toPrint = toPrint[:-1]

    print(toPrint)

spaces = 0
for i in range(n - 1, -1, -1):
    spaces += 2
    toPrint = " " * spaces

    for j in range(i + 1):
        toPrint += str(j) + " "

    for j in range(i - 1, -1, -1):
        toPrint += str(j) + " "

    toPrint = toPrint[:-1]

    print(toPrint)
