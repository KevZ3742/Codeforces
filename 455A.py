# A. Boredom
# https://codeforces.com/contest/455/problem/A
# rating: 1500

n = int(input())
a = list(map(int, input().split()))

count = dp = [0] * (max(a) + 1)
for num in a:
    count[num] += 1

dp[0] = 0
dp[1] = count[1]

for i in range(2, len(count)):
    dp[i] = max(dp[i - 1], dp[i - 2] + count[i] * i)

print(dp[-1])