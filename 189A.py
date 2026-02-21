# A. Cut Ribbon
# https://codeforces.com/contest/189/problem/A
# rating: 1300

n, a, b, c = map(int, input().split())

dp = [-1] * (n + 1)
dp[0] = 0

for i in range(min(a, b, c), n + 1):
    if i >= a:
        dp[i] = max(dp[i], dp[i - a] + 1)
    if i >= b:
        dp[i] = max(dp[i], dp[i - b] + 1)
    if i >= c:
        dp[i] = max(dp[i], dp[i - c] + 1)

    if dp[i] == 0:
        dp[i] = -1

print(dp[n])