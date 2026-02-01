# https://codeforces.com/problemset/problem/34/A
# rating: 800

n = int(input())
a = list(map(int, input().split()))

minHeight = float('inf')

toPrint = [0, 0]
prev = a[-1]
for i in range(n):
    temp = min(minHeight, abs(a[i] - prev))

    if temp < minHeight:
        minHeight = temp
        toPrint = [i - 1, i]

    prev = a[i]

if toPrint[0] == -1:
    toPrint[0] = n - 1

if toPrint[1] == -1:
    toPrint[1] = n - 1

toPrint[0] += 1
toPrint[1] += 1

print(*toPrint)