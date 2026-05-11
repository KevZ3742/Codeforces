# F. Forever Winter
# https://codeforces.com/problemset/problem/1829/F
# rating: 1300

from collections import Counter

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    edges = []

    for i in range(m):
        u, v = map(int, input().split())
        edges.append(u)
        edges.append(v)

    edgeCounter = Counter(edges)
    valueCounter = Counter(edgeCounter.values())
    sortedValueCounter = valueCounter.most_common()

    if sortedValueCounter[-1][1] != 1:
        print(sortedValueCounter[-1][0], sortedValueCounter[-1][0] - 1)
    else:
        print(sortedValueCounter[-1][0], sortedValueCounter[-2][0] - 1)