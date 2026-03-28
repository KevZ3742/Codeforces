# A. New Year Transportation
# https://codeforces.com/contest/500/problem/A
# rating: 1000

n, t = map(int, input().split())
a = list(map(int, input().split()))
 
i = 0
 
while i < t - 1:
    i += a[i]
 
if i == t - 1:
    print("YES")
else:
    print("NO")