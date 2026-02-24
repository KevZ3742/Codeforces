# A. Sorting Game
# https://codeforces.com/problemset/problem/2190/A
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    sortedS = sorted(s)

    if list(s) == sortedS:
        print("Bob")
        continue

    toPrint = []

    for i in range(n):
        if s[i] != sortedS[i]:
            toPrint.append(i + 1)

    print("Alice")
    print(len(toPrint))
    print(*toPrint)
    