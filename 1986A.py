# A. X Axis
# https://codeforces.com/problemset/problem/1986/A
# rating: 800

def f(x1, x2, x3, chosen):
    return abs(x1 - chosen) + abs(x2 - chosen) + abs(x3 - chosen) 

t = int(input())

for _ in range(t):
    x1, x2, x3 = map(int, input().split())

    if x1 == x2 or x1 == x3:
        chosen = x1
    elif x2 == x3:
        chosen = x2
    else:
        chosen = sorted([x1, x2, x3])[1]

    print(f(x1, x2, x3, chosen))