# B. Sequence Game
# https://codeforces.com/problemset/problem/1862/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    toPrint = [b[0]]

    prev = b[0]
    for i in range(1, n):
        if prev <= b[i]:
            toPrint.append(b[i])
        else:
            toPrint.append(b[i])
            toPrint.append(b[i])

        prev = b[i]

    print(len(toPrint))
    print(*toPrint)