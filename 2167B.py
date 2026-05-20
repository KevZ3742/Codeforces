# B. Your Name
# https://codeforces.com/problemset/problem/2167/B
# rating: 800

from collections import Counter

q = int(input())

for _ in range(q):
    n = int(input())
    a, b = input().split()

    if Counter(a) == Counter(b):
        print("YES")
    else:
        print("NO")
