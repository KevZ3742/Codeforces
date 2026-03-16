# C2. Powering the Hero (hard version)
# https://codeforces.com/contest/1800/problem/C2
# rating: 1100

import heapq
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    h = []
    power = 0
 
    for num in s:
        if num == 0:
            if h:
                power += -heapq.heappop(h)
        else:
            heapq.heappush(h, -num)
 
    print(power)