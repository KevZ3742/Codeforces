# A. Magnets
# https://codeforces.com/contest/344/problem/A
# rating: 800

n = int(input())

groups = 0
prev = -1
for _ in range(n):
    curr = int(input())
    if curr != prev:
        groups += 1
    prev =  curr
    
print(groups)