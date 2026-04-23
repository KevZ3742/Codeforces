# A. Buttons
# https://codeforces.com/problemset/problem/1858/A
# rating: 800

import math

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    anna = a + math.ceil(c // 2)
    katie = b + c // 2

    if anna > katie:
        print("First")
        continue
    if anna == katie:
        if (a + b + c) % 2:
            print("First")
        else:
            print("Second")
    else:
        print("Second")