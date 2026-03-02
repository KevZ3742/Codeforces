# B. Make it Zigzag
# https://codeforces.com/problemset/problem/2154/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    currMax = -1
    for i in range(n):
        if a[i] > currMax:
            currMax = a[i]

        if i % 2:
            a[i] = currMax

    toPrint = 0
    for i in range(1, n, 2):
        if i == 1:
            toPrint += max(0, a[i - 1] - a[i] + 1)
            continue

        toPrint += max(0, a[i - 1] - a[i] + 1, a[i - 1] - a[i - 2] + 1)
        
    if n % 2:
        toPrint += max(0, a[-1] - a[-2] + 1)

    print(toPrint)

