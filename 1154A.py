# A. Restoring Three Numbers
# https://codeforces.com/problemset/problem/1154/A
# rating: 800

nums = list(map(int, input().split()))

nums.sort()

print(nums[3] - nums[0], nums[3] - nums[1], nums[3] - nums[2])