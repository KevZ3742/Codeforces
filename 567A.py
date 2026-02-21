# A. Lineland Mail
# https://codeforces.com/contest/567/problem/A
# rating: 900

n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    if i == 0:
        minCost = x[1] - x[0]
    elif i == n - 1:
        minCost = x[n - 1] - x[n - 2]
    else:
        minCost = min(x[i + 1] - x[i], x[i] - x[i - 1])
        
    maxCost = max(x[-1] - x[i], x[i] - x[0])

    print(minCost, maxCost)