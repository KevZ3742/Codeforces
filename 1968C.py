# C. Assembly via Remainders
# https://codeforces.com/problemset/problem/1968/C
# rating: 1000

t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    toPrint = [0] * n
    toPrint[0] = 10**6

    for i in range(1, n):
        toPrint[i] = toPrint[i-1] + a[i-1]
    
    print(*toPrint)