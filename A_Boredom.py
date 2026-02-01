# rating: 1500

n = int(input())
a = list(map(int, input().split()))

count = [0] * (max(a) + 1)
for _ in a:
    count[_] += 1

dp = [0] * len(count)

dp[0] = 0
dp[1] = count[1]

for i in range(2, len(count)):
    dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)

print(dp[-1])