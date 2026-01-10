# https://codeforces.com/problemset/problem/455/A
# rating: 1500

n = int(input())
a = list(map(int, input().split()))

count = [0] * (max(a) + 1)
for _ in a:
    count[_] += 1

memo = {}

def dp(i):
    if i == 0:
        return 0
    elif i == 1:
        return count[1]
    
    if i in memo:
        return memo[i]
    
    memo[i] = max(dp(i-1), dp(i-2) + count[i] * i)
    return memo[i]
    
print(dp(max(a)))

# wip