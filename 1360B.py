# B. Honest Coach
# https://codeforces.com/problemset/problem/1360/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    toPrint = a[-1] - a[0]

    for i in range(n):
        for j in range(i + 1, n):
            toPrint = min(toPrint, a[j] - a[i])

    print(toPrint)