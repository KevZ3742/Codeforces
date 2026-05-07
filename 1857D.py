# D. Strong Vertices
# https://codeforces.com/problemset/problem/1857/D
# rating: 13000

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    diffArr = []
    for i in range(n):
        diffArr.append(a[i] - b[i])

    target = max(diffArr)
    toPrint = []

    for i in range(n):
        if diffArr[i] == target:
            toPrint.append(i + 1)

    print(len(toPrint))
    print(*toPrint)
