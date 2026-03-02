# B. MEX Reordering
# https://codeforces.com/problemset/problem/2191/B
# rating: 1000

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a.count(0) == 0:
        print("NO")
    elif a.count(0) == 1:
        print("YES")
    elif a.count(0) >= 2 and a.count(1) >= 1:
        print("YES")
    else: 
        print("NO")
    