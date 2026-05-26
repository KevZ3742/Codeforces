# A. Make it Beautiful
# https://codeforces.com/problemset/problem/1783/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    if a[0] == a[-1]:
        print("NO")
    else:
        print("YES")
        print(a[-1], *a[:n - 1])