# A. Binary Matrix
# https://codeforces.com/problemset/problem/2082/A
# rating: 800

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = []
    for i in range(n):
        r = list(map(int, input().strip()))
        a.append(r)

    r = 0
    for i in range(n):
        xor = 0
        for j in range(m):
            xor ^= a[i][j]
        
        if xor:
            r += 1

    c = 0
    for j in range(m):
        xor = 0
        for i in range(n):
            xor ^= a[i][j]
        
        if xor:
            c += 1

    print(max(r, c))