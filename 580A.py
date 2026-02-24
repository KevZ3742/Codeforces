# A. Kefa and First Steps
# https://codeforces.com/problemset/problem/580/A
# rating: 900

n = int(input())
a = list(map(int, input().split()))

maxLen = 1
curr = 1
for i in range(1, n):
    if a[i] >= a[i - 1]:
        curr += 1
    else:
        curr = 1
    
    maxLen = max(maxLen, curr)

print(maxLen)