# B. Array Craft
# https://codeforces.com/problemset/problem/1990/B
# rating: 1200

t = int(input())
 
for _ in range(t):
    n, x, y = map(int, input().split())
 
    xArr = [-1] * n
    yArr = [-1] * n
 
    for i in range(x):
        xArr[i] = 1
 
    for i in range(n - (y - 1)):
        yArr[i] = 1
 
    yArr = yArr[::-1]
 
    toPrint = []
    for i in range(n):
        if xArr[i] == -1 or yArr[i] == -1:
            toPrint.append(-1)
        else:
            toPrint.append(1)
 
    print(*toPrint)

    # wa