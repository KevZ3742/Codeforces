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