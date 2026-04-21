# B. Bulk Blocks
# https://codeforces.com/group/EW9LgKVDr6/contest/687333/problem/B

import math

row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
type1 = list(map(int, input().split()))
type2 = list(map(int, input().split()))
type3 = list(map(int, input().split()))
h = list(map(int, input().split()))
s = list(map(int, input().split()))

rows = row1 + row2 + row3
types = type1 + type2 + type3

mapp = {}
for i in range(27):
    mapp[types[i]] = mapp.get(types[i], 0) + rows[i]

for i in range(9):
    mapp[s[i]] = mapp.get(s[i], 0) + h[i]

freeSlots = 27
for v in mapp.values():
    freeSlots -= math.ceil(v / 64)

if freeSlots >= 0:
    print("YES")
else:
    print("NO")