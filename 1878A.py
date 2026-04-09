# A. How Much Does Daytona Cost?
# https://codeforces.com/problemset/problem/1878/A
# rating: 800

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k not in a:
        print("NO")
    else:
        print("YES")