# A. Required Remainder
# https://codeforces.com/problemset/problem/1374/A
# rating: 800

t = int(input())
 
for _ in range(t):
    x, y, n = map(int, input().split())
    
    toPrint = n - n % x + y
    if toPrint > n:
        print(n - n % x - (x - y))
    else:
        print(toPrint)