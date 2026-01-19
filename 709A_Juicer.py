# https://codeforces.com/contest/709/problem/A
# rating: 900

n, b, d = map(int, input().split())
a = list(map(int, input().split()))

emptyCount = 0
waste = 0
for i in a:
    if i > b:
        continue
    else:
        waste += i

    if waste > d:
        emptyCount += 1
        waste = 0

print(emptyCount)