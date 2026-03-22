# B. Array
# https://codeforces.com/contest/2209/problem/B
# rating: ?

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    toPrint = []
    for i in range(n):
        greater = sum(1 for j in range(i+1, n) if a[j] > a[i])
        lesser  = sum(1 for j in range(i+1, n) if a[j] < a[i])
        toPrint.append(max(greater, lesser))
    print(*toPrint)