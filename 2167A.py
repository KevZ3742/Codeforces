# A. Square?
# https://codeforces.com/problemset/problem/2167/A
# rating: 800

t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    if a == b == c == d:
        print("YES")
    else:
        print("NO")