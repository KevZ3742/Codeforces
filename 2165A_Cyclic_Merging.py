# https://codeforces.com/contest/2165/problem/A
# rating: 1300

from collections import deque

# t = int(input())

for _ in range(t):
    n = int(input())
    a = deque(list(map(int, input().split())))

    cost = 0
    
    lowestPair = 0
    lowestSum = float('inf')
    for i in range(a):
        


# dq = deque([1, 2, 3, 4, 5])
# dq.rotate(-2)
# print(list(dq))