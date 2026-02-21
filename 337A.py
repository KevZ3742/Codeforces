# A. Puzzles
# https://codeforces.com/contest/337/problem/A
# rating: 900

n, m = map(int, input().split())
f = list(map(int, input().split()))

f.sort()

i = 0
minDifference = float('inf')
while n + i <= m:
    curr = f[i:n + i]
    minDifference = min(minDifference, curr[-1] - curr[0])
    i += 1

print(minDifference)