# D. Gold Rush
# https://codeforces.com/problemset/problem/1829/D
# rating: 1000

def solve(n, m, dp):
    if n == m:
        return True

    if n < m or n % 3 != 0:
        return False
    
    if n in dp:
        return dp[n]
    
    l = n * 2 // 3
    r = n // 3

    dp[n] = solve(l, m, dp) or solve(r, m, dp)
    return dp[n]

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    dp = {}

    if solve(n, m, dp):
        print("YES")
    else:
        print("NO")