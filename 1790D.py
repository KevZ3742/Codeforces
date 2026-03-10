# D. Matryoshkas
# https://codeforces.com/problemset/problem/1790/D
# rating: 1200

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    counter = Counter(a)

    toPrint = 0
    for num in sorted(counter):
        toPrint += max(0, counter[num] - counter.get(num - 1, 0))

    print(toPrint)

# tle