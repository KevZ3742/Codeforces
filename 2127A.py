# A. Mix Mex Max
# https://codeforces.com/problemset/problem/2127/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a = [num for num in a if num != -1]

    if len(set(a)) <= 1 and not a.count(0):
        print("YES")
    else:
        print("NO")

    
        