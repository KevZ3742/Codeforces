# https://codeforces.com/contest/2184/problem/C
# rating: ?

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if k > n:
        print(-1)
        continue

    if k == n:
        print(0)
        continue

    splits = [n]

    if n % 2 == 0:
        splits.add(n // 2)
    else:
        splits.add(n // 2)
        splits.add(n // 2 + 1)
    
# wip
        
