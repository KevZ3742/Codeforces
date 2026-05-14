# B. Optimal Reduction
# https://codeforces.com/problemset/problem/1713/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    operations = max(a)
    
    curOperations = a[0]
    for i in range(1, n):
        if a[i-1] < a[i]:
            curOperations += a[i] - a[i-1]
    
    if curOperations == operations:
        print("YES")
    else:
        print("NO")