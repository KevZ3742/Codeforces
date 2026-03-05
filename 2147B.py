# B. Multiple Construction
# https://codeforces.com/problemset/problem/2147/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = []
    for i in range(n, 0, -1):
        toPrint.append(i)

    toPrint.append(n)

    for i in range(1, n):
        toPrint.append(i)
    
    print(*toPrint)