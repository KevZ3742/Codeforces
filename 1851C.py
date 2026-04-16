# C. Tiles Comeback
# https://codeforces.com/problemset/problem/1851/C
# rating: 1000

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    if c[0] == c[-1]:
        if c.count(c[0]) >= k:
            print("YES")
        else:
            print("NO")
    else:
        a = b = 0
        l = 0
        r = n - 1
        while l <= r:
            if c[l] == c[0]:
                a += 1
            if c[r] == c[-1]:
                b += 1

            if a >= k and b >= k:
                print("YES")
                break

            if a < k:
                l += 1
            if b < k:
                r -= 1
        else:
            print("NO")