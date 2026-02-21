# D. OutOfMemoryError
# https://codeforces.com/contest/2185/problem/D
# rating: 1100

t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())
    a = list(map(int, input().split()))
    
    arr = a.copy()
    lastUpdate = [-1] * n
    lastReset = -1

    for i in range(m):
        b, c = map(int, input().split())
        b -= 1

        if lastUpdate[b] <= lastReset:
            arr[b] = a[b]

        arr[b] += c

        lastUpdate[b] = i

        if arr[b] > h:
            lastReset = i

    toPrint = []
    for i in range(n):
        if lastUpdate[i] > lastReset:
            toPrint.append(arr[i])
        else:
            toPrint.append(a[i])
    
    print(*toPrint)