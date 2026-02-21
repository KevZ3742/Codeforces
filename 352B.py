# B. Jeff and Periods
# https://codeforces.com/contest/352/problem/B
# rating: 1300

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

values = defaultdict(lambda: [True, -1, -1])

for i in range(n):
    curr = a[i]

    if not values[curr]:
        continue

    if values[curr][1] != -1 and values[curr][2] == -1:
        values[curr][2] = i - values[curr][1]

    if values[curr][2] != -1 and i - values[curr][1] != values[curr][2]:
        values[curr][0] = False
        continue
    
    values[curr][1] = i

valid = 0
toPrint = []
for key in values.keys():
    if values[key][0]:
        valid += 1
        toPrint.append([key, max(values[key][2], 0)])

print(valid)
toPrint.sort()
for i in toPrint:
    print(*i)