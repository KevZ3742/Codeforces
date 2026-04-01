# A. Painting With Two Colors
# https://codeforces.com/problemset/problem/2134/A
# rating: 800

t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    if (n  + b) % 2 == 1:
        print("NO")
        continue

    if b >= a:
        print("YES")
    else:
        if (n  + a) % 2 == 1:
            print("NO")
        else:
            print("YES")