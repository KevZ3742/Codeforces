# B. Monsters
# https://codeforces.com/problemset/problem/1849/B
# rating: 1000

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    indexedList = []

    for i in range(n):
        r = a[i] % k
        if r == 0:
            r = k
        indexedList.append((i + 1, r))

    indexedList.sort(key=lambda x: (-x[1], x[0]))

    toPrint = []
    for idx, val in indexedList:
        toPrint.append(idx)

    print(*toPrint)