# C. Ski Resort
# https://codeforces.com/problemset/problem/1840/C
# rating: 1000

t = int(input())

for _ in range(t):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))

    groups = []
    days = 0
    for num in a:
        if num <= q:
            days += 1
        else:
            groups.append(days)
            days = 0

    groups.append(days)

    combinations = 0
    for days in groups:
        toAdd = days * (days + 1) // 2
        toSubtract = days * (days + 1) // 2 - (days - k + 1) * (days - k + 2) // 2

        if days >= k:
            combinations += toAdd - toSubtract

    print(combinations)
        