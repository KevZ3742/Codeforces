# C. Loyalty
# https://codeforces.com/problemset/problem/2161/C
# rating: 1200

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    points = 0
    order = []
    s = 0

    l, r = 0, n - 1
    while l <= r:
        if s + a[r] >= x:
            s = (s + a[r]) % x
            points += a[r]

            order.append(a[r])
            r -= 1
        else:
            s += a[l]

            order.append(a[l])
            l += 1

    print(points)
    print(*order)