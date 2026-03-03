# C. Assembly via Minimums
# https://codeforces.com/problemset/problem/1857/C
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    b.sort()

    a = []
    prevMax = b[0]
    marker = 0
    for i in range(n - 1, 0, -1):
        if b[marker] > prevMax:
            prevMax = b[marker]

        a.append(prevMax)
        marker += i

    a.append(prevMax)

    print(*a)