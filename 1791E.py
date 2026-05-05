# E. Negatives and Positives
# https://codeforces.com/problemset/problem/1791/E
# rating: 1100

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    numNeg = 0
    for num in a:
        if num < 0:
            numNeg += 1

    for i in range(n):
        a[i] = abs(a[i])

    if numNeg % 2:
        a.sort()
        print(sum(a) - 2 * a[0])
    else:
        print(sum(a))