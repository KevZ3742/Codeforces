# A. Perfect Root
# https://codeforces.com/contest/2185/problem/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = ""
    for i in range(1, n + 1):
        toPrint += str(i) + " "

    print(toPrint)