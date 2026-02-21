# B. Unlucky Ticket
# https://codeforces.com/contest/160/problem/B
# rating: 1100

n = int(input())
s = list(input())

a, b = s[:n], s[n:]
a.sort()
b.sort()

strictlyMore = True
strictlyLess = True
for i in range(n):
    if a[i] >= b[i]:
        strictlyLess = False
    
    if a[i] <= b[i]:
        strictlyMore = False

if strictlyMore or strictlyLess:
    print("YES")
else:
    print("NO")