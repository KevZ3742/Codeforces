# D. Super-Permutation
# https://codeforces.com/problemset/problem/1822/D
# rating: 1200 

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
        continue

    if n % 2:
        print(-1)
        continue

    toPrint = []
    for i in range(n):
        if i % 2:
            toPrint.append(i)
        else:
            toPrint.append(n - i)

    print(*toPrint)