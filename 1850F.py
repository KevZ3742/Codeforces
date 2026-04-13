# F. We Were Both Children
# https://codeforces.com/problemset/problem/1850/F
# rating: 1300 

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = [0] * (n + 1)
    for i in a:
        if i <= n:
            count[i] += 1

    toPrint = [0] * (n + 1)
    for i in range(1, n + 1):
        if count[i] > 0:
            for multiple in range(i, n + 1, i):
                toPrint[multiple] += count[i]
    
    print(max(toPrint))