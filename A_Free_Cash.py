# A. Free Cash
# https://codeforces.com/problemset/problem/237/A
# rating: 1000

from collections import Counter

n = int(input())

times = []
for _ in range(n):
    h, m =map(int, input().split())
    times.append((h, m))

timesCounter = Counter(times)

print(max(timesCounter.values()))