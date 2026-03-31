# D. 1D Eraser
# https://codeforces.com/problemset/problem/1873/D
# rating: 800

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    i = 0
    toPrint = 0
    
    while i < n:
        if s[i] == 'B':
            toPrint += 1
            i += k
        else:
            i += 1
    
    print(toPrint)