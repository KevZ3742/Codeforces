# C. Removal of Unattractive Pairs
# https://codeforces.com/problemset/problem/1907/C
# rating: 1200

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    sCounter = Counter(s)
    toPrint = max(2 * max(sCounter.values()) - n, 1 if n & 1 else 0)

    print(toPrint)