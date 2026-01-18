# https://codeforces.com/contest/2185/problem/D
# rating: ?

t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())
    a = list(map(int, input().split()))
    
    arr = a.copy()

    for i in range(m):
        b, c = map(int, input().split())
        b -= 1

        arr[b] += c

        if arr[b] > h:
            arr = a.copy()

    print(*arr)

# tle