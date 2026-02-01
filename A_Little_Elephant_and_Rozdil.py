# https://codeforces.com/problemset/problem/205/A
# rating: 900

from collections import Counter

n = int(input())
a = list(map(int, input().split()))

aCounter = Counter(a)
minTime = min(aCounter.keys())

if aCounter[minTime] > 1:
    print("Still Rozdil")
else:
    print(a.index(minTime) + 1)