# C. Less or Equal
# https://codeforces.com/contest/977/problem/C
# rating: 1200

n, k = map(int, input().split())
a = sorted(map(int, input().split()))
 
if k == 0:
    if a[0] == 1:
        print(-1)
    else:
        print(a[0] - 1)
elif n == k or a[k - 1] != a[k]:
    print(a[k - 1])
else:
    print(-1)