# A. Array Coloring
# https://codeforces.com/problemset/problem/1857/A
# rating: 800

t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if (sum(a) - a[0]) % 2 == a[0] % 2:
        print("YES")
    else:
        print("NO")