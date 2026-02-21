# B. Fence
# https://codeforces.com/contest/363/problem/B
# rating: 1100

n, k = map(int, input().split())
a = list(map(int, input().split()))

height = sum(a[:k])
minHeight = height
minHeightIndex = 0
for i in range(n - k):
    height += a[i + k] - a[i]
    temp = min(minHeight, height)
    if minHeight > temp:
        minHeight = temp
        minHeightIndex = i + 1

print(minHeightIndex + 1)