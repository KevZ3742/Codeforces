# B. Interesting drink
# https://codeforces.com/problemset/problem/706/B
# rating: 1100

n = int(input())
x = sorted(map(int, input().split()))
q = int(input())

for _ in range(q):
    m = int(input()) 

    l, r = 0, n
    while l < r:
        mid = (l + r) // 2
        if x[mid] <= m:
            l = mid + 1
        else:
            r = mid

    print(l)
    