# C. And?
# https://codeforces.com/contest/2214/problem/C

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))

    xor_sum = nums[0] ^ nums[1] ^ nums[2]

    nums.sort()
    median = nums[1]
    
    result = xor_sum - median
    
    print(result)