# rating: 1100

from collections import Counter

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

bCounts = Counter(b)

counterA = 0
counterB = 0

comparisons = 1
r = n - 1
for l in range(n):
    if a[l] in bCounts:
        counterA += comparisons * bCounts[a[l]]

    if a[r] in bCounts:
        counterB += comparisons * bCounts[a[r]]
    
    r -= 1
    comparisons += 1

print(counterA, counterB)