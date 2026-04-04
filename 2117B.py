# B. Shrink
# https://codeforces.com/problemset/problem/2117/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = []
    for i in range(1, n + 1, 2):
        toPrint.append(i)
    
    if n % 2:
        n -= 1

    for i in range(n, 0, -2):
        toPrint.append(i)

    print(*toPrint)