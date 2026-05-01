# A. Plus One on the Subset
# https://codeforces.com/problemset/problem/1624/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    print(a[-1] - a[0])