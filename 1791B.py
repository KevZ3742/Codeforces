# B. Following Directions
# https://codeforces.com/problemset/problem/1791/B
# rating: 800

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    x = 0
    y = 0

    for i in s:
        if i == "L":
            x -= 1
        if i == "R":
            x += 1
        if i == "D":
            y -= 1
        if i == "U":
            y += 1
        if x == 1 and y == 1:
            print("YES")
            break
    else:
        print("NO")