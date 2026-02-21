# B. Sale
# https://codeforces.com/contest/34/problem/B
# rating: 900

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

earnings = 0
for i in range(m):
    if a[i] < 0:
        earnings += a[i]

print(abs(earnings))