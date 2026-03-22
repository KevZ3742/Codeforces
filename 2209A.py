# A. Flip Flops
# https://codeforces.com/contest/2209/problem/A
# rating: ?

t = int(input())
for _ in range(t):
    n, c, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    
    for i in range(n):
        if a[i] > c:
            break

        use = min(k, c - a[i])
        k -= use
        c += a[i] + use
    
    print(c)