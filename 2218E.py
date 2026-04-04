# E. The 67th XOR Problem
# https://codeforces.com/contest/2218/problem/E
# rating: ?

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, a[i] ^ a[j])
    
    print(best)