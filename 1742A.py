# A. Sum
# https://codeforces.com/problemset/problem/1742/A
# rating: 800

t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    
    maxA = a.index(max(a))
    if a[maxA] - a[maxA - 1] == a[maxA - 2]:
        print("YES")
    else:
        print("NO")