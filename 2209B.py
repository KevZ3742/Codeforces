# B. Array
# https://codeforces.com/contest/2209/problem/B
# rating: ?

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    toPrint = []

    for i in range(n):
        greater = 0
        lesser = 0

        for j in range(i + 1, n):
            if a[j] > a[i]:
                greater += 1
            elif a[j] < a[i]:
                lesser += 1

        toPrint.append(max(greater, lesser))

    print(*toPrint)