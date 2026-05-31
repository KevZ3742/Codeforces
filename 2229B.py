# B. Absolute Cinema
# https://codeforces.com/problemset/problem/2229/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    toPrint = 0
    garbage = []

    for i in range(n):
        toPrint += max(a[i], b[i])
        garbage.append(min(a[i], b[i]))

    toPrint += max(garbage)

    print(toPrint)