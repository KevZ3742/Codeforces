# C. Array Game
# https://codeforces.com/problemset/problem/1904/C
# rating: 1400

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))

    if k >= 3:
        print(0)
        continue

    toPrint = a[0]
    for i in range(n - 1):
        diff = a[i+1] - a[i]
        if diff < toPrint:
            toPrint = diff

    if k == 1:
        print(toPrint)
        continue

    for i in range(n):
        for j in range(i + 1, n):
            diff = a[j] - a[i]

            l, h = 0, n - 1
            while l <= h:
                m = (l + h) // 2

                currDiff = abs(a[m] - diff)
                if currDiff < toPrint:
                    toPrint = currDiff

                if a[m] < diff:
                    l = m + 1
                elif a[m] > diff:
                    h = m - 1
                else:
                    toPrint = 0
                    break
        
            if toPrint == 0:
                break
        if toPrint == 0:
                break
        
    print(toPrint)