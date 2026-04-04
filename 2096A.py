# A. Wonderful Sticks
# https://codeforces.com/problemset/problem/2096/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    s = "_" + input()

    toPrint = [0] * n
    curr = n
    for i in range(n - 1, -1, -1):
        if s[i] == ">":
            toPrint[i] = curr
            curr -= 1

    for i in range(n):
        if toPrint[i] == 0:
            toPrint[i] = curr
            curr -= 1

    print(*toPrint)