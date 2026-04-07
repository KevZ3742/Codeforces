# A. Halloumi Boxes
# https://codeforces.com/problemset/problem/1903/A
# rating: 800

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if a == sorted(a):
        print("YES")
        continue

    if k > 1:
        print("YES")
    else:
        print("NO")

