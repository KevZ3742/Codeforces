# C. War Strategy
# https://codeforces.com/contest/2183/problem/C
# rating: 1500

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    l = 0
    r = 0
    while True:
        tried = False

        if l < k - 1 and l + r + max(l + 1, r) <= m:
            l += 1
            tried = True

        if r < n - k and l + r + max(l, r + 1) <= m:
            r += 1
            tried = True

        if not tried:
            break

    print(l + r + 1)