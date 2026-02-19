# B. Sereja and Suffixes
# https://codeforces.com/problemset/problem/368/B
# rating: 1100

n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * n
distinct = set()
for i in range(n - 1, -1, -1):
    distinct.add(a[i])
    dp[i] = len(distinct)

for _ in range(m):
    l = int(input()) - 1

    print(dp[l])
