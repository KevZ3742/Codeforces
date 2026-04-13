# A. K-divisible Sum
# https://codeforces.com/problemset/problem/1476/A
# rating: 1000

import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    x = 1
    if n > k:
        x = math.ceil(n / k)
    
    print(math.ceil(k * x / n))