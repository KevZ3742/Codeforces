# D. Three Activities
# https://codeforces.com/problemset/problem/1914/D
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    sortedA = sorted(range(n), key=lambda i: a[i], reverse=True)[:3]
    sortedB = sorted(range(n), key=lambda i: b[i], reverse=True)[:3]
    sortedC = sorted(range(n), key=lambda i: c[i], reverse=True)[:3]

    toPrint = 0
    for x in sortedA:
        for y in sortedB:
            for z in sortedC:
                if x != y and x != z and y != z:
                    toPrint = max(toPrint, a[x] + b[y] + c[z])
                                        
    print(toPrint)