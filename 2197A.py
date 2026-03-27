# A. Friendly Numbers
# https://codeforces.com/problemset/problem/2197/A
# rating: 800

t = int(input())

for _ in range(t):
    x = int(input())
    count = 0
    
    for s in range(1, 91):
        y = x + s
        if sum(map(int, str(y))) == s:
            count += 1
    
    print(count)