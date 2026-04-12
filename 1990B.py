# B. Array Craft
# https://codeforces.com/problemset/problem/1990/B
# rating: 1200
 
t = int(input())
 
for _ in range(t):
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1

    l = []
    temp = -1
    for i in range(y):
        l.append(temp)
        temp *= -1
    l = l[::-1]    

    m = [1] * (x - y + 1)
    
    r = []
    temp = -1
    for i in range(n - x - 1):
        r.append(temp)
        temp *= -1

    print(*(l + m + r))