# B. Two Out of Three
# https://codeforces.com/problemset/problem/1894/B
# rating: 1000

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    aCounter = Counter(a)
    greaterThan2 = [k for k, v in aCounter.items() if v >= 2]

    if len(greaterThan2) < 2:
        print(-1)
        continue

    first, second = greaterThan2[:2]

    toPrint = []
    used = {first: 0, second: 0}

    for x in a:
        if x == first:
            if used[first] == 0:
                toPrint.append(1)
                used[first] += 1
            elif used[first] == 1:
                toPrint.append(2)
                used[first] += 1
            else:
                toPrint.append(1)
        elif x == second:
            if used[second] == 0:
                toPrint.append(1)
                used[second] += 1
            elif used[second] == 1:
                toPrint.append(3)
                used[second] += 1
            else:
                toPrint.append(1)
        else:
            toPrint.append(1)

    print(*toPrint)
