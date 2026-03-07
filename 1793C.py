# C. Dora and Search
# https://codeforces.com/problemset/problem/1793/C
# rating: 1200

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    minA = 1
    maxA = n

    lFound, rFound = False, False
    l, r = 0, n - 1
    while l < r:
        if a[l] == minA:
            l += 1
            minA += 1
            lFound = False
        elif a[l] == maxA:
            l += 1
            maxA -= 1
            lFound = False
        else:
            lFound = True

        if lFound and rFound:
            break
        
        if a[r] == minA:
            r -= 1
            minA += 1
            rFound = False
        elif a[r] == maxA:
            r -= 1
            maxA -= 1
            rFound = False
        else:
            rFound = True
    else:
        print(-1)
        continue
        
    print(l + 1, r + 1)