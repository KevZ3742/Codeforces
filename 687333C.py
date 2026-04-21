# C. Challenging Encounter
# https://codeforces.com/group/EW9LgKVDr6/contest/687333/problem/C

import math
 
n, a, b, x, y, z = map(int, input().split())
 
attacksToKill = math.ceil(a / y)
damage = attacksToKill * b
 
hp = x
for i in range(n):
    hp -= damage 
 
    if hp <= 0:
        print("NO")
        break
 
    hp = min(x, hp + z)
else:
    print("YES")