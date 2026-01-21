# https://codeforces.com/contest/799/problem/A
# rating: 1100

import math

n, t, k, d = map(int, input().split())


timeNoOven = 0
timeNoOven = math.ceil(n / k)
timeNoOven *= t

time = 0
oven1time = 0
oven2time = 0
startOven2 = False
while n > 0:
    time += 1
    oven1time += 1

    if startOven2:
        oven2time += 1

    if time >= d:
        startOven2 = True

    if oven1time == t:
        n -= k
        oven1time = 0

    if oven2time == t:
        n -= k
        oven2time = 0

if timeNoOven <= time:
    print("NO")
else:
    print("YES")