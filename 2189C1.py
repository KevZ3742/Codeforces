# C1. XOR Convenience (Easy Version)
# https://codeforces.com/problemset/problem/2189/C1
# rating: 1300

t = int(input())

for _ in range(t):
    n = int(input())

    toPrint = [0] * n

    if n % 2:
        toPrint[0] = n - 1
    else:
        toPrint[0] = n

    toPrint[-1] = 1

    for i in range(1, n - 1):
        if i % 2:
            toPrint[i] = i + 2
        else:
            toPrint[i] = i
    
    print(*toPrint)