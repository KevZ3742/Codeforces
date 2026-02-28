# D. Portal
# https://codeforces.com/contest/2200/problem/D
# rating: ?

t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    p = list(map(int, input().split()))
    
    mid = p[x:y]
    mid = mid[min(mid):] + mid[:min(mid)]

    outer = p[:x] + p[y:]

    if not outer:
        print(*mid)
        continue
    
    for i in range(len(outer)):
        if outer[i] > mid[0]:
            print(*(outer[:i] + mid + outer[i:]))
            continue