# B. Burglar and Matches
# https://codeforces.com/contest/16/problem/B
# rating: 900

from collections import defaultdict

n, m = map(int, input().split())

matches = defaultdict(int)
for _ in range(m):
    a, b = map(int, input().split())
    matches[b] += a

sortedMatches = sorted(matches.keys(), reverse=True)

toPrint = 0
for box in sortedMatches:
    if n == 0:
        break

    boxesToTake = min(n, matches[box])
    toPrint += boxesToTake * box
    n -= boxesToTake

print(toPrint)