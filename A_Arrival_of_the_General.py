# https://codeforces.com/problemset/problem/144/A
# rating: 800

n = int(input())
a = list(map(int, input().split()))

aMax = max(a)
aMin = min(a)
aMaxIndex = a.index(aMax)
aMinIndex = len(a) - 1 - a[::-1].index(aMin)

if aMaxIndex > aMinIndex:
    swaps = -1
else:
    swaps = 0

swaps += n - aMinIndex + aMaxIndex - 1

print(swaps)