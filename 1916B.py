# B. Two Divisors
# https://codeforces.com/problemset/problem/1916/B
# rating: 1000 

import math

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    lcm = math.lcm(a, b)

    if b % a == 0:
        lcm = math.lcm(a, b) * b / a

    print(int(lcm))