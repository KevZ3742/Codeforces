# F. The 67th Tree Problem
# https://codeforces.com/contest/2218/problem/F
# rating: ?

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    n = x + y

    if x == y == 0:
        print("YES")
        continue

    if y == 0:
        print("NO")
        continue

    if x > y:
        print("NO")
        continue

    if x == 0 and y % 2 == 0:
        print("NO")
        continue

    print("YES")

    if x == 0:
        for i in range(2, y + 1):
            print(1, i)
    elif n % 2 == 0:
        for i in range(1, 2 * x):
            print(i, i + 1)
        for i in range(2 * x + 1, n + 1):
            print(1, i)
    else:
        for i in range(1, 2 * x + 1):
            print(i, i + 1)
        for i in range(2 * x + 2, n + 1):
            print(1, i)