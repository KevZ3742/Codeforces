# B. Corner Twist
# https://codeforces.com/problemset/problem/1983/B
# rating: 1200

t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
    
    a = []
    for i in range(n):
        line = list(map(int, input()))
        a.append(line)

    b = []
    for i in range(n):
        line = list(map(int, input()))
        b.append(line)

    if a == b:
        print("YES")
        continue

    aRowSums = [0] * n
    aColSums = [0] * m
    bRowSums = [0] * n
    bColSums = [0] * m

    for i in range(n):
        for j in range(m):
            aRowSums[i] += a[i][j]
            aColSums[j] += a[i][j]
            bRowSums[i] += b[i][j]
            bColSums[j] += b[i][j]

    flag1 = True
    for i in range(n):
        if aRowSums[i] % 3 != bRowSums[i] % 3:
            flag1 = False
            break

    flag2 = True
    for i in range(m):
        if aColSums[i] % 3 != bColSums[i] % 3:
            flag2 = False
            break

    if flag1 and flag2:
        print("YES")
    else:
        print("NO")