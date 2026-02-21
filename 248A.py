# A. Cupboards
# https://codeforces.com/contest/248/problem/A
# rating: 800

from collections import Counter

n = int(input())

left = Counter()
right = Counter()
for _ in range(n):
    l, r = map(int, input().split())
    
    left[l] += 1
    right[r] += 1

openAll = left[0] + right[0]
closeAll = left[1] + right[1]
allLeft = left[0] + right[1]
allRight = left[1] + right[0]

print(min(openAll, closeAll, allLeft, allRight))