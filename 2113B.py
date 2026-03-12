# B. Good Start
# https://codeforces.com/problemset/problem/2113/B
# rating: 1200

t = int(input())

for _ in range(t):
    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    if x1 == x2:
        if abs(y2 - y1) % b == 0:
            print("Yes")
        else:
            print("No")
        continue

    if y1 == y2:
        if abs(x2 - x1) % a == 0:
            print("Yes")
        else:
            print("No")
        continue

    if abs(y2 - y1) % b == 0 or abs(x2 - x1) % a == 0:
        print("Yes")
    else:
        print("No")