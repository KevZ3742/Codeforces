# B. Ordinary Numbers
# https://codeforces.com/problemset/problem/1520/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())

    s = str(n)
    length = len(s)

    toPrint = (length - 1) * 9
    first = int(s[0])
    ordinary = int(s[0] * length)

    toPrint += first - 1
    
    if ordinary <= n:
        toPrint += 1
    
    print(toPrint)