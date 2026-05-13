# A. Maximum Increase
# https://codeforces.com/problemset/problem/702/A
# rating: 800

n = int(input())
a = list(map(int, input().split()))

maxLen = 0
cur = 1
for i in range(1, n):
    if a[i - 1] < a[i]:
        cur += 1
    else:
        maxLen = max(cur, maxLen)
        cur = 1

maxLen = max(cur, maxLen)

print(maxLen)