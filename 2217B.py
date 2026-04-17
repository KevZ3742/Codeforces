# B. Flip the Bit (Easy Version)
# https://codeforces.com/contest/2217/problem/B
# rating: 1000

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))

    pivot = p[0]
    arr = [0] * (n + 2)

    for i in range(1, n + 1):
        arr[i] = a[i - 1]

    arr[0] = arr[n + 1] = arr[pivot]

    countL = 0
    countR = 0

    for i in range(0, pivot):
        if arr[i] != arr[i + 1]:
            countL += 1

    for i in range(pivot, n + 1):
        if arr[i] != arr[i + 1]:
            countR += 1

    print(max(countL, countR))