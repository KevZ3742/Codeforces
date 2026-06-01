# B. Gifts Fixing
# https://codeforces.com/problemset/problem/1399/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mina = min(a)
    minb = min(b)

    ans = 0
    for i in range(n):
        ans += max(a[i] - mina, b[i] - minb)

    print(ans)