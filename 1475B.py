# B. New Year's Number
# https://codeforces.com/problemset/problem/1475/B
# rating: 900

t = int(input())

for _ in range(t):
    n = int(input())
    
    toUse = n // 2020
    n -= toUse * 2020
    
    if n <= toUse:
        print("YES")
    else:
        print("NO")