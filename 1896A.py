# A. Jagged Swaps
# https://codeforces.com/problemset/problem/1896/A
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] == 1:
        print("YES")
    else:
        print("NO")