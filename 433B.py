# B. Kuriyama Mirai's Stones
# https://codeforces.com/contest/433/problem/B
# rating: 1200

n = int(input())
a = list(map(int, input().split()))
m = int(input())

dp = [0] * (n + 1)
for i in range(n):
    dp[i + 1] = dp[i] + a[i]

aSorted = sorted(a)
dpSorted = [0] * (n + 1)
for i in range(n):
    dpSorted[i + 1] = dpSorted[i] + aSorted[i]

for _ in range(m):
    type, l, r = map(int, input().split())

    if type == 1:
        print(dp[r] - dp[l - 1])
    else:
        print(dpSorted[r] - dpSorted[l-1])