# https://codeforces.com/problemset/problem/318/A
# rating: 900

n, k = map(int, input().split())

k += 1
evenStartIndex = 0

if n % 2 == 0:
    evenStartIndex = n // 2
else:
    evenStartIndex = n // 2 + 1

toPrint = k - evenStartIndex

# wip